# -*- coding: utf-8 -*-
import scrapy

from items import Product

class AldiSpider(scrapy.Spider):
    name = 'freshfarms'
    allowed_domains = ['freshfarms.com']
    start_urls = ['https://www.freshfarms.com/weekly-specials/']

    def parse(self, response):
        items = []
        if response.css("main").css(".elementor-widget-wrap"):
            products = response.css("main").css("section:not(.elementor-hidden-tablet)").css(".elementor-widget-wrap .elementor-widget-wrap")
            if products != None:
                for product in products:
                    if len(product.css(".elementor-element")) > 2 and product.css("img").css("::attr(src)").get() != None:
                        title = product.css(".elementor-element")[1].css("h2::text").get()
                        price = product.css(".elementor-element")[2].css("h2::text").get()
                        item = Product()
                        item['product_url'] = ''
                        item['title'] = title.strip()
                        item['price'] = price != None and price.strip()
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

        store_object = {'store_name':'freshfarms', 'items':items}

        return store_object