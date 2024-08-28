import requests
from bs4 import BeautifulSoup
import random
import time
import csv

useragents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4894.117 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4855.118 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4892.86 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4854.191 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4859.153 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36/null",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36,gzip(gfe)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4895.86 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4860.89 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4885.173 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4864.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4877.207 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.133 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4872.118 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4876.128 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
]

header = {
    "User-Agent": None,
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

def connect(url):
    header["User-Agent"] = useragents[random.randrange(len(useragents))]
    resp = requests.get(url, headers=header)
    print(header["User-Agent"])
    if resp.status_code != 200:
        print(resp)
        return None
    
    return resp


def get_title(bs_obj):
    try:
        item_title = bs_obj.find("span", {"id": "productTitle"}).text.strip() 
        if len(item_title) > 25:
            item_title = item_title[:25] + "..."
    except:
        item_title = None
    # if first css selector failed try this one
    if item_title == None:
        item_title = bs_obj.css.select("h1#title.a-spacing-none.a-text-normal") 
        print(item_title)

    return item_title

def get_price(bs_obj):
    try:
        p = bs_obj.css.select("#buyBoxAccordion")[0]
    except IndexError:
        try: #use nested try except clause to account for different html structure on different amazon pages
            p = bs_obj.css.select(".a-section.a-spacing-none.a-padding-none")[0]
        except IndexError:
            return None

    price = p.find("span", {"class": "a-offscreen"}).text.strip()
    if price == "":
        price = p.find("span", {"class": "a-price"}).text.strip()

    price = float(price[1:]) #remove dollar sign and convert to float
    print(price)
    return price

def get_image(bs_obj):
    try:
        images = bs_obj.find_all("div", {"class": "imgTagWrapper"})
        img_addr = images[0].find("img")["src"]
    except:
        img_addr = None

    return img_addr

def get_rating(bs_obj):
    try:
        rating = bs_obj.find("span", {"class": "a-icon-alt"}).text
    except:
        rating = None

    return rating

def clear_csv():
    with open('product_info.csv', 'w') as csv_file:
        csv_file.write("")


def output_csv(product_list):
    with open("product_info.csv", "a") as csv_file:
        fieldnames = ["title", "image", "price", "rating", "url"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for p in product_list:
            writer.writerow(p)

def read_url_file():
    with open('item_urls.txt') as url_file:
        url_list = [url.strip('\n') for url in url_file]

    return url_list



def get_product_info():
    products = []

    url_list = read_url_file()
    if(len(url_list) == 0):
        print('list is empty')
        exit(1)

    #make connection for each url in url_list
    for item_url in url_list:
        resp = connect(item_url)
        soup = BeautifulSoup(resp.text, "html.parser").body

        obj = {
            "title": get_title(soup),
            "image": get_image(soup),
            "price": get_price(soup),
            "rating": get_rating(soup),
            "url": item_url
        }

        products += [obj]
        time.sleep(random.randrange(6, 30))
    
    return products
