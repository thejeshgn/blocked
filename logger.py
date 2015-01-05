import sys
import sqlite3 as lite
import requests
import time
from BeautifulSoup import BeautifulSoup
import dataset
import time
from datetime import datetime
import json
import csv
import easygui

    
#TODO: implement this using API
def getISPDetails():
    log = {}
#    log["ISP"]= "Atria Convergence Technologies Pvt. Ltd."
#    log["IP"]=  "103.227.96.80"
#    log["ISP_SHORT"]=  "ACT"    
#    log["IP_LOCATION"]= "India, Karnataka, Bangalore"
    log["ISP"]= "Bharti Airtel Limited"
    log["IP"]=  "106.216.197.16"
    log["ISP_SHORT"]=  "Airtel4G"    
    log["IP_LOCATION"]= "India, Karnataka, Bangalore"

    return log


#TODO: get the rules for blocking_rules.json and apply it instead of
#TODO: hardcoding the rules like below
def checkForISP(isp, content):
    soup = BeautifulSoup(content)
    title = soup.find('title')
    
    if isp == "Atria Convergence Technologies Pvt. Ltd.":
        if title and len(title.contents) > 0:
            if str(title.contents[0]) == "URL Blocked!":
                return "BLOCKED"
            else:
                return "CANT DECIDE"
        else:
            return "CANT DECIDE"
    if isp == "Bharti Airtel Limited":
        if content == "This website/URL has been blocked until further notice either pursuant to Court orders or on the Directions issued by the Department of Telecommunications":
            return "BLOCKED"
        else:
            return "CANT DECIDE"
            
def runRequests():
    first_row = True
    with open("MASTER_LIST.csv", 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if first_row:
                first_row  = False
                continue
            line = row[1]
            #each line is a link
            url_dict = {}
            url = str(line).strip()
            print "Trying ="+(url)
            results = URL_TABLE.find_one(URL=url, ISP_SHORT=isp['ISP_SHORT'], RUN_NAME=RUN_NAME)
            if results:
                print "Exists"
                continue
            r = None
            try:
                r = requests.get(url)        
            except requests.exceptions.Timeout:
                # Maybe set up for a retry, or continue in a retry loop
                url_dict["STATUS"]= "UNREACHABLE, Timeout"
            except requests.exceptions.TooManyRedirects:
                # Tell the user their URL was bad and try a different one
                url_dict["STATUS"]= "UNREACHABLE, TooManyRedirects"

            except requests.exceptions.RequestException as e:
                # catastrophic error. bail.
                url_dict["STATUS"]= "UNREACHABLE, RequestException"

        
            url_dict['URL']=url

            if r:
                if r.status_code == 200:
                    content = r.content
                    status = checkForISP(isp['ISP'], content)
                    url_dict["STATUS"]=status            
                else:
                    url_dict["STATUS"]= "UNREACHABLE, HTTP STATUS ="+str(r.status_code)

            url_dict.update(isp)
            start_time= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            url_dict["RUN_NAME"]=RUN_NAME
            url_dict["RUN_TIME"]=start_time
            print url_dict  
            URL_TABLE.insert(url_dict)
            db.commit()
            time.sleep(1)

if __name__ == "__main__":
    RUN_NAME = "FIRST_RUN"
    db = dataset.connect('sqlite:///./database/db.sqlite')
    URL_TABLE = db['URLS']
    isp = getISPDetails()

    msg = "Is this a Re-run or Fresh Run?"
    choices = ["Rerun","Fresh"]
    reply = easygui.buttonbox(msg,  choices=choices)
    if reply == "Fresh":
        if easygui.ynbox('We will clear everything to do a fresh start. Continue?', 'Fresh Start', ('Yes', 'No')):
            URL_TABLE.delete()
            runRequests()
        else:
            easygui.msgbox("You seemed to be confused so ending here. Restart")
    else:
        runRequests()
