# _*_coding : uft-8 _*_
# @Time : 2022-10-17 19:40
# @Author : 崔奕斐
# @File : 爬取十页
# @Project : Python基础
import urllib.parse
import urllib.request
import  json
import jsonpath
import re
import csv
import requests
def create_request(page):
    base_url = 'https://www.zhihu.com/api/v4/creators/rank/hot?domain=0&'
    data = {

        'limit' : 20,
        'offset': (page-1)*20,

    }
    u = '&period=hour'

    data = urllib.parse.urlencode(data)
    url = base_url + data + u



    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko)Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'}
    request = urllib.request.Request(url = url,headers = headers)
    return request

def get_content(request):
  response = urllib.request.urlopen(request)
  content = response.read().decode('utf-8')
  return content

def down_load(page,content):
    with open('zhihuyaoqiude' + str(page) +'.json','w',encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
 start_page = int(input('请输入起始的页码'))
 end_page = int(input('请输入结束的页码'))
 for page in range(start_page,end_page+1):
    #每一页都有自己的请求
     request = create_request(page)



    #获取相应数据
     content = get_content(request)
    #下载
     down_load(page,content)
     a = str(page)
 with open('zhihu.csv', mode='a', encoding='utf-8', newline='') as f:
     csv_wirter = csv.writer(f)
     csv_wirter.writerow(['url_list1'])


 obj = json.load(open('zhihuyaoqiude'+a +'.json', 'r', encoding='utf-8'))
 #obj = json.load(open('zhihuyaoqiude1.json', 'r', encoding='utf-8'))
 url_list1 = jsonpath.jsonpath(obj, '$..url')
 url_list2 = jsonpath.jsonpath(obj, '$..title')
 url_list3 = url_list1 = jsonpath.jsonpath(obj, '$..name')
 url_list4 = url_list1 = jsonpath.jsonpath(obj, '$..score')
 print(url_list1)
 print(url_list2)
 print(url_list3)
 print(url_list4)

 with open('zhihu.csv',mode='a',encoding='utf-8',newline='') as f:
     csv_wirter = csv.writer(f)
     csv_wirter.writerow([url_list1])








