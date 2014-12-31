import sys
import sqlite3 as lite
import requests
import time
from BeautifulSoup import BeautifulSoup
import dataset
import time
from datetime import datetime
import json

RUN_NAME = "FIRST_RUN"
    
#TODO: implement this using API
def getISPDetails():
    log = {}
    log["ISP"]= "Atria Convergence Technologies Pvt. Ltd."
    log["IP"]=  "103.227.96.80"
    log["ISP_SHORT"]=  "ACT"    
    log["IP_LOCATION"]= "India, Karnataka, Bangalore"
    return log


#TODO:get the rules for error_msgs
def checkForISP(isp, content):
    soup = BeautifulSoup(content)
    title = soup.find('title')
    if title and len(title.contents) > 0:
        if str(title.contents[0]) == "URL Blocked!":
            return "BLOCKED"
        else:
            return "CANT DECIDE"
    else:
        return "CANT DECIDE"

db = dataset.connect('sqlite:///./database/db.sqlite')
URL_TABLE = db['URLS']
with open("urls.txt") as f:
    for line in f:
        #each line is a link
        url_dict = {}
        url = str(line).strip()
        print "Trying ="+(url)
        results = URL_TABLE.find_one(URL=url, RUN_NAME=RUN_NAME)
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
        isp = "Atria Convergence Technologies Pvt. Ltd."
        if r:
            if r.status_code == 200:
                content = r.content
                status = checkForISP(isp, content)
                url_dict["STATUS"]=status            
            else:
                url_dict["STATUS"]= "UNREACHABLE, HTTP STATUS ="+str(r.status_code)

        url_dict.update(getISPDetails())
        start_time= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        url_dict["RUN_NAME"]=RUN_NAME
        url_dict["RUN_TIME"]=start_time
        print url_dict  
        URL_TABLE.insert(url_dict)
        db.commit()
        time.sleep(1)

