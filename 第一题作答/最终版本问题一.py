# _*_coding : uft-8 _*_
# @Time : 2022-10-19 0:37
# @Author : 崔奕斐
# @File : 最终版本
# @Project : Python基础
#1.发送请求
import requests
import re
import json
import csv
import time
import random
import pymysql

def save_sql(url,title,name,score):
 con = pymysql.connect(
    host = '49.235.100.87',
    port = 3306,
    user = 'root'
    password = 'root'
    db = '知乎数据'
 )
 db = con.cursor()
 sql = f'insert into goods(url,title,name,score) values ("{url}","{title}","{name}","{score}")'
 db.execute(sql)

 con.commit()
 db.close()
#1.定制请求
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.'
                        '36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'}
for page in rage(1,11):
url = f'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&limit=20&{(page-1*20)}period=hour'
with open('zhihu.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_wirter = csv.writer(f)
    csv_wirter.writerow(['url', 'title', 'name', 'score'])

#2.获取数据
response = requests.get(url = url, headers =headers)
html_data = response.text
print(response.text)


#3.解析数据
json_str = html_data
json_dict = json.loads(json_str)


auctions = json_dict[0]['data']['question']
for auction in auctions:
    url = print(auction[url])
    title = print(auction[title])
    name = print(auction[topics][name])
    print(url,title,name)

scores = json_dict[1]['reaction']['score']
for score in scores:
    score = print(score[score])
    print(score)
save_sql(url,title,name,score)

#4.保存数据
 with open('zhihu.csv', mode='a', encoding='utf-8', newline='') as f:
     csv_wirter = csv.writer(f)
     csv_wirter.writerow([url,title,name,score])

time.sleep(random.randint(3,5))


