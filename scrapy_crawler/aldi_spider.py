# -*- coding: utf-8 -*-
import scrapy

from items import Product

class AldiSpider(scrapy.Spider):
    name = 'aldi'
    allowed_domains = ['aldi.us']
    start_urls = ['https://www.aldi.us/weekly-specials/this-weeks-aldi-finds/']

    def price(self, product):
        current_price = ''
        decimal = ''
        asterisk = ''
        base_price = ''

        if product.css(".box--price").css(".box--value") != None:
            current_price = product.css(".box--price").css(".box--value::text").get()
        if product.css(".box--price").css(".box--decimal") != None:
            decimal = product.css(".box--price").css(".box--decimal::text").get()
        if product.css(".box--price").css(".box--asterisk") != None:
            asterisk = product.css(".box--price").css(".box--asterisk::text").get()
        if product.css(".box--price").css(".box--baseprice") != None:
            base_price = product.css(".box--price").css(".box--baseprice::text").get()
        if base_price == None:
            base_price = ''

        return f'{current_price}{decimal} {asterisk} {base_price}'

    def parse(self, response):
        items = []
        if response.css("article"):
            product_urls = response.css("article").css("a[title='to product detail']").css("::attr(href)").getall()
            if product_urls and len(product_urls) > 0:
                for product_url in product_urls:
                    item = Product()
                    item['product_url'] = product_url
                    product = response.css("article").css("a[href='" + product_url + "']")
                    if product:
                        item['title'] = product.css(".box--description--header::text").get().strip()
                        item['price'] = self.price(product)
                        item['image_url'] = product.css("img").css("::attr(src)").get()
                    items.append(item)
            else:
                item = Product()
                item['product_url'] = 'not found'
                item['title'] = 'not found'
                item['price'] = 'not found'
                item['image_url'] = 'not found'
                items.append(item)
        else:
            item = Product()
            item['product_url'] = 'not found'
            item['title'] = 'not found'
            item['price'] = 'not found'
            item['image_url'] = 'not found'
            items.append(item)

        return {'store_name':'aldi', 'items':items}