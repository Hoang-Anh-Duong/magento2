import scrapy


class LinhkiendientuSpider(scrapy.Spider):
    name = 'linhkiendientu'
    # allowed_domains = ['www.phucanh.vn/linh-kien-pc-lap-rap.html']
    start_urls = ['file:///home/nam/Desktop/Project/tmdt/datacrawler/example.html']

    def parse(self, response):
      # page = response.url.split("/")[-2]?
      filename = 'example.html'
      with open(filename, 'wb') as f:
          f.write(response.body)
