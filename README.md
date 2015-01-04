# Blocked

Blocked by ISPs in India

##Install dependencies
`git clone https://github.com/thejeshgn/blocked`

`cd blocked`

`sudo xargs -a requirements.txt pip install`


## MASTER_LIST.csv
Master list of all the sites blocked in India. With the source and other details. Cretaed out of the lists. [MASTER_LIST.csv](https://github.com/thejeshgn/blocked/blob/master/MASTER_LIST.csv) .

## Lists: Source of Blocked URL
Lists are simple textfiles with urls. Name of the file becomes the source name. We create a file everytime we get news of somesite getting blocked.

- kafila_maste_list.txt - [List published by Kafila](http://kafila.org/2012/05/26/list-of-websites-blocked-in-india/)
- blocked-websites-MSM-world-cup.txt - [List published by Medianama](http://www.medianama.com/wp-content/uploads/blocked-websites-MSM-world-cup.txt)
- medianama2.txt - [By the article list published by Medianama](http://www.medianama.com/2014/07/223-world-cup-2014-472-websites-including-google-docs-blocked-in-india-following-sony-complaint/)
- toi_govt_block_32_websites.txt - [List published by ToI](http://timesofindia.indiatimes.com/tech/tech-news/Pastebin-Dailymotion-Github-blocked-after-DoT-order-Report/articleshow/45701713.cms)



## Code
### Create master List
- Run python create_master_list.py
- It will merge all the lists and create an unique list with source details. Called [MASTER_LIST.csv](https://github.com/thejeshgn/blocked/blob/master/MASTER_LIST.csv)

### Logger
It goes through the MASTER_LIST.csv and checks if its been actually blocked by some rules. **Its work in progress**.

### APIS
- http://ipaddress.com/
- http://www.whatismyip.com/
- http://www.iplocation.net/
- http://www.ip2location.com/demo

### TODO
- Make it based on rules
- Implement API to get ISP details
- Add the details about the source, date of addition etc
