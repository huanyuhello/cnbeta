import scrapy
class TestSpider(scrapy.Spider):
    name = "test"

    start_urls = [
        "http://www.cnbbeta.com/",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
