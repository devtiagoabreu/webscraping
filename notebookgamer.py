import scrapy


class NotebookgamerSpider(scrapy.Spider):
    name = "notebookgamer"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebook-gamer?sb=rb#D[A:notebook%20gamer]"]

    def parse(self, response):
        pass
