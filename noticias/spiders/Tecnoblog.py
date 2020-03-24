# -*- coding: utf-8 -*-
import scrapy


class TecnoblogSpider(scrapy.Spider):
    name = 'Tecnoblog'
    allowed_domains = ['booking.com']
    start_urls = ['https://www.booking.com/hotel/br/fazenda-vista-alegre.pt-br.html']

    def parse(self, response):
        for img in response.xpath("//div[contains(@id,'photos_distinct')]/a"):
            imagem = img.css("a::attr(href)").extract_first()
            titulo = img.css("a::attr(title)").extract_first()
            yield {'Title':titulo,'Imagem':imagem}
