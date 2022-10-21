# _*_coding : uft-8 _*_
# @Time : 2022-10-21 21:22
# @Author : 崔奕斐
# @File : 有效版
# @Project : Python基础
#start_urls = ['https://www.bkjx.sdu.edu.cn/https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=154&PAGENUM={}&urltype=tree.TreeTempUrl&wbtreeid=1010'.format(0*15) for num in range(6)]

 #   def parse(self, response):
  #    urls = response.xpath('//div[@style="float:left"]/a').get_attribute('href').extract()
   #   titles = response.xpath('//div[@style="float:left"]').extract()
    #  times = response.xpath('//div[@style="float:right;"]').extract()
import urllib.request
from lxml import etree
def create_request(page):
    url = 'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=154&PAGENUM='+ str(page) +'&urltype=tree.TreeTempUrl&wbtreeid=1010'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.10171 SLBChan/103'}
    request = urllib.request.Request(url=url, headers=headers)
    return request
def get_content(request):
  response = urllib.request.urlopen(request)
  content = response.read().decode('utf-8')
  print(content)
  return content

def down_load(content):
    tree = etree.HTML(content)

    titles = tree.xpath('//div[@style="float:left"]')
    times = tree.xpath('//div[@style="float:right;"]')
    urls = tree.xpath('//div[@style="float:left"]/a')


    for title in titles:
        print(title)
    for time in times:
        print(time)
    for url in urls:
        print(url)




if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
       #（1）请求对象定制
        request = create_request(page)
       #（2）获取网页源码
        content = get_content(request)
        #print(content)
       #(3)下载
        down_load(content)

