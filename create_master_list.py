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
db = dataset.connect('sqlite:///./database/db.sqlite')
MASTER_LIST= db['MASTER_LIST']

    
for files in ['blocked-websites-MSM-world-cup.txt', 'kafila_maste_list.txt', 'medianama2.txt', 'toi_govt_block_32_websites.txt']:
    file_path = "./lists/"+files
    with open(file_path) as f:
        for line in f:
            url_dict = {}
            URL = str(line).strip()
            print URL
            SOURCE =  str(files)
            results = MASTER_LIST.find_one(URL=URL)
            if results:
                print "Exists"
                continue
            else:
                url_dict['URL']=URL
                url_dict['SOURCE']=SOURCE
                MASTER_LIST.insert(url_dict)
                db.commit()

result = db['MASTER_LIST'].all()
dataset.freeze(result, format='csv', filename='MASTER_LIST.csv')
                
    