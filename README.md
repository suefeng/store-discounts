# Store Discounts

This is a web scraper tool to help you find store discounts. It uses [Scrapy](https://scrapy.org/) to scrape the stores discount pages.

## Currently supported stores

- [Aldi USA](https://www.aldi.us/weekly-specials/this-weeks-aldi-finds/)
- [Fresh Farms](https://www.freshfarms.com/weekly-specials/)

## WIP

- [Marianos](https://www.marianos.com/weeklyad/shoppable)

## Required dependencies

- Python
- [pipenv](https://pipenv.pypa.io/en/latest/) `2023.12.1`
- [http-server](https://www.npmjs.com/package/http-server)

## To set up and run the app

1. Install the packages using `pipenv install`.
2. Then run `bash run.sh` or `zsh run.sh` to generate the products listing and run the server.
3. Check that `products.json` gets created.
4. Navigate to http://localhost:8080 to view the store discounts page.

## To run the app without generating a new product listing

1. Run `npx http-server`
2. Navigate to http://localhost:8080 to view the store discounts page.

## To crawl and generate a product listing without running the http server

1. `cd scrapy_crawler`
2. `scrapy runspider aldi_spider.py -o products.json`
