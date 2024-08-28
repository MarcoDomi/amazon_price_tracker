import web_scraper

#only execute this script if product_info.csv is empty
product_list = web_scraper.get_product_info()
web_scraper.clear_csv()
web_scraper.output_csv(product_list)
