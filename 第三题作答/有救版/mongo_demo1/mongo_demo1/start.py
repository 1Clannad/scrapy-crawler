# _*_coding : uft-8 _*_
# @Time : 2022-10-20 23:41
# @Author : 崔奕斐
# @File : start
# @Project : mongo_demo1
from scrapy.cmdline import execute

execute('scrapy crawl moyan'.split())
from scrapy import cmdline

def update():

# 把爬虫程序放在这个类里 是爬虫的name

cmdline.execute('scrapy crawl maoyan spider'.split())

# 想几点更新,定时到几点

def time_ti(h=17, m=54):

while True:

now = datetime.datetime.now()

# print(now.hour, now.minute)

if now.hour == h and now.minute == m:

doSth()

# 每隔60秒检测一次

time.sleep(60)

time_ti()