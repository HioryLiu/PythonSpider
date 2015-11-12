#UTF-8

from scrapy.spiders import CrawlSpider


class douban(CrawlSpider):

    name="douban"
    start_urls=['http://movie.douban.com/chart']

    def parse(self, response):
        print response.body
        a= response.body
        b=response.url
