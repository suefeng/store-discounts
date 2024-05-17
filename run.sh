#!/bin/bash
cd scrapy_crawler;
rm -rf products_data
scrapy runspider aldi_spider.py -o products_data/aldi_products.json;
scrapy runspider marianos_spider.py -o products_data/marianos_products.json;
scrapy runspider freshfarms_spider.py -o products_data/freshfarms_products.json;

awk 'BEGIN{print "["} FNR > 1 && last_file == FILENAME {print line} FNR == 1 {line = ""} FNR==1 && FNR != NR {printf ","} FNR > 1 {line = $0} {last_file = FILENAME} END{print "]"}' products_data/* > products.json

cd ..;
npx http-server;
open http://localhost:8080;
