# -*- coding: utf-8 -*-
import scrapy

from items import Product
from scrapy_playwright.page import PageMethod

class MarianosSpider(scrapy.Spider):
    name = 'marianos'
    allowed_domains = ['www.marianos.com']
    # start_urls = ['https://www.marianos.com/weeklyad/shoppable']

    def start_requests(self):
        url = 'https://www.marianos.com/weeklyad/shoppable'
        yield scrapy.Request(url, meta={
            "playwright": True, 
            "playwright_page_methods": [
                PageMethod("wait_for_selector", ".BestDealsDesktopGrid"),
            ],
        })

    def price(self, product):
        pricePrefix = product.css(".SWA-OmniPricePrefix::text").get()
        price = product.css(".FeaturePriceHeading").css("attr(aria-label)").get()
        return f'{pricePrefix} {price}'.strip()

    def parse(self, response):
        items = []
        dealWrapper = response.css(".BestDealsDesktopGrid")
        print('dealWrapper: ', dealWrapper)
        if dealWrapper != None:
            products = dealWrapper.css(".kds-Card")
            if products and len(products) > 0:
                for product in products:
                    item = Product()
                    item['product_url'] = ''
                    if product:
                        item['title'] = product.css(".FeatureDealDescription::text").get().strip()
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

        store_object = {'store_name':'marianos', 'items':items}

        yield store_object