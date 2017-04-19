# Blocked

Crowdsourced list of all the websites blocked by ISPs in India. 


## MASTER_LIST.csv
Master list of all the sites blocked in India. With the source and other details. Cretaed out of the lists. [MASTER_LIST.csv](https://github.com/thejeshgn/blocked/blob/master/MASTER_LIST.csv) .

## Lists: Source of Blocked URL
Lists are simple textfiles with urls. Name of the file becomes the source name. We create a file everytime we get news of somesite getting blocked.

- kafila_maste_list.txt - [List published by Kafila](http://kafila.org/2012/05/26/list-of-websites-blocked-in-india/)
- blocked-websites-MSM-world-cup.txt - [List published by Medianama](http://www.medianama.com/wp-content/uploads/blocked-websites-MSM-world-cup.txt)
- medianama2.txt - [By the article list published by Medianama](http://www.medianama.com/2014/07/223-world-cup-2014-472-websites-including-google-docs-blocked-in-india-following-sony-complaint/)
- toi_govt_block_32_websites.txt - [List published by ToI](http://timesofindia.indiatimes.com/tech/tech-news/Pastebin-Dailymotion-Github-blocked-after-DoT-order-Report/articleshow/45701713.cms)
- yourbroadband.txt - [List published by Youbroadband](http://www.youbroadband.in/List%20of%20Blocked%20Websites-Regulatory%20Guidelines%20&%20HighCourt%20Orders.pdf)
- india_music_industry_104_sites.txt - [The Indian Music Industry, a consortium of 142 music companies, announced today that it has obtained orders from the Calcutta High Court directing all Internet Service Providers (387 in all) to block access to 104 music sites from India.](http://www.medianama.com/2012/03/223-list-of-104-music-sites-that-the-indian-music-industry-wants-blocked/)
- madras_court_order_kabali_forum_sites.txt, madras_court_order_kabali_streaming_sites.txt, madras_court_order_kabali_torrent_sites.txt [As per Madras High Court order pertaining to Kabaali](http://www.actcorp.in/madras_court_order-kabali.pdf)



## Code
### Create master List
- Run python create_master_list.py
- It will merge all the lists and create an unique list with source details. Called [MASTER_LIST.csv](https://github.com/thejeshgn/blocked/blob/master/MASTER_LIST.csv)
- I plan to add other features and henec a script to merge. 


### Install dependencies
`git clone https://github.com/thejeshgn/blocked`

`cd blocked`

`sudo xargs -a requirements.txt pip install`
