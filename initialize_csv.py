import web_scraper

# only execute this script if product_info.csv is empty

#add file lines to a single string
with open("item_urls.txt") as f:
    url_str = ""
    for line in f:
        url_str += line
        
url_list = url_str.splitlines() #removes new line char at end of url

if len(url_list) > 0:
    product_list = web_scraper.get_product_info(url_list)
    web_scraper.clear_csv()
    web_scraper.output_csv(product_list)
else:
    print("URL file is empty.")
