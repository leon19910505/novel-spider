import scrapy
from pachong.items import BookItem, ContentItem

from scrapy.http import Request


class DingDianSpider(scrapy.Spider):
    name = "dingdian"
    # allowed_domains = ["dmoz.org"]
    urls = []
    for i in range(10):
        urls = urls + ["http://www.23us.so/files/article/html/19/%d/index.html" % i]
    start_urls = urls

    def parse(self, response):

        book = BookItem()
        for str in response.xpath('//div[@class="bdsub"]/dl/dt/a[3]/text()').extract():
            book['name'] = str
        for str in response.xpath('//div[@class="bdsub"]/dl/dd[2]/h3/text()').extract():
            book['author'] = str

        urls = response.xpath('//td[@class="L"]/a//@href').extract()
        for url in urls:
            yield Request(url, self.chapterMethod, meta={'book':book},dont_filter=True)
        yield book

    def chapterMethod(self, response):

        book = response.meta['book']
        content = ContentItem()
        content['name'] = book['name']
        content['chapter'] = response.xpath('//div[@id="amain"]/dl/dd[1]/h1/text()').extract()[0]
        content['content'] = response.xpath('/html/body/div[@id="a_main"]/div[@id="amain"]/dl/dd[@id="contents"]/text()').extract()
        yield content
