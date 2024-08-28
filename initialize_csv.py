import web_scraper

#only execute this script if product_info.csv is empty

url_list = []
with open("item_urls.txt") as f:
    for line in f:
        url_list.append(line.strip('\n'))
        
if len(url_list) > 0:
    product_list = web_scraper.get_product_info(url_list)
    web_scraper.clear_csv()
    web_scraper.output_csv(product_list)
else:
    print("URL file is empty.")
