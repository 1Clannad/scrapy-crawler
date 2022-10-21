import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['www.bkjx.sdu.edu.cn']
    start_urls = ['https://www.bkjx.sdu.edu.cn/https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=154&PAGENUM={}&urltype=tree.TreeTempUrl&wbtreeid=1010'.format(0*15) for num in range(6)]

    def parse(self, response):
      urls = response.xpath('//div[@style="float:left"]/a').get_attribute('href').extract()
      titles = response.xpath('//div[@style="float:left"]').extract()
      times = response.xpath('//div[@style="float:right;"]').extract()
      for url, title, time in zip(urls, titles, times):
        yield
        {
          'urls': url,
          'titles' : title,
          'times' : time
        }
