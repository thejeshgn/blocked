import sys
import sqlite3 as lite
import requests
import time
from BeautifulSoup import BeautifulSoup
import dataset
import time
from datetime import datetime
import json
t = datetime.now()
start_time= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log = {}
log["TIME_START"]= str(start_time),


    
#implement this
def getISPDetails():
    log["ISP"]= "Atria Convergence Technologies Pvt. Ltd.",
    log["ISP"]=  "103.227.96.80",
    log["IP_LOCATION"]= "India, Karnataka, Bangalore",
    return log


#get the rules for error_msgs
def checkForISP(isp, content):
    soup = BeautifulSoup(content)
    title = soup.find('title')
    if title == "URL Blocked!":
        return "BLOCKED"
    else:
        return "CANT DECIDE"

URLS = []
log.update(getISPDetails())

with open("urls.txt") as f:
    for line in f:
        #each line is a link
        url_dict = {}
        url = str(line).strip()
        r = requests.get(url)
        url_dict['URL']=url
        if r.status_code == 200:
            content = r.content
            isp = "Atria Convergence Technologies Pvt. Ltd."
            status = checkForISP(isp, content)
            url_dict["STATUS"]=status
        else:
            url_dict["STATUS"]= "UNREADCHABLE, HTTP STATUS ="+str(r.status_code)
        print url_dict    
        URLS.append(url_dict) 
log['URLS']=URLS
            
            
            
end_time= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log["TIME_END"] = end_time
end_time_log_file_name= "status_log_"+str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))+".json"

f = open('myfile','w')
f.write(json.dumps(log))
f.close() 