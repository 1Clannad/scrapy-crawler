# _*_coding : uft-8 _*_
# @Time : 2022-10-19 9:14
# @Author : 崔奕斐
# @File : 最终版本问题三
# @Project : Python基础
import requests
import re
import json
import csv
import time
import random
import pymysql
def save_sql(url,title,time):
 con = pymysql.connect(
    host = '49.235.100.87',
    port = 3306,
    user = 'root'
    password = 'root'
    db = '学校官网数据'
 )
 db = con.cursor()
 sql = f'insert into goods(url,title,time) values ("{url}","{title}","{time}")
 db.execute(sql)

 con.commit()
 db.close()

 # 1.定制请求
url = f'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=154&PAGENUM=4&{page}urltype=tree.TreeTempUrl&wbtreeid=1010'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'}
for page in rage(1,6):
with open('sdu官网.csv', mode='a', encoding='utf-8', newline='') as f
    csv_wirter = csv.writer(f)
    csv_wirter.writerow(['url', 'title', 'time'])
    url = f'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=154&PAGENUM={page}&urltype=tree.TreeTempUrl&wbtreeid=1010'
#2.获取数据
response = requests.get(url=url, headers=headers)
html_data = response.text
print(response.text)

#3.解析数据
json_str = re.findall('language=(.*);',html_data)[0]
json_dict = json.loads(json_str)
auctions = json_dict['language']

for auction in auctions:
    url = print(auction[href])
    title = print(auction[title])
    time = print(auction[>])
    print(url,title,time)
    save_sql(url, title,time)

#4.保存数据
 with open('sdu官网.csv', mode='a', encoding='utf-8', newline='') as f:
     csv_wirter = csv.writer(f)
     csv_wirter.writerow([url,title,time])


time.sleep(random.randint(3,5))

