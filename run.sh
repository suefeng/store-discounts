#!/bin/bash
cd scrapy_crawler;
rm products.json;
scrapy runspider aldi_spider.py -o products.json;
cd ..;
npx http-server;
open http://localhost:8080;
