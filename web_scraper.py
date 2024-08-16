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

item_list = [
    "https://www.amazon.com/EverFoam-Womens-Slippers-Memory-Lightweight/dp/B09JP2TRK4/ref=sr_1_17?crid=ZBF39A8404BL&dib=eyJ2IjoiMSJ9.fEuf3e7C2_6gIYiJfKcd8ndDNiMKcCrQjhuSTWdW-bIxJ6qmZjfTxzFgjkMtuSinq1n3mQpW3MjNbyywq6Ypmp1bKrS_skzoEUIJuNowmxiXTNt6rqzG9yFFkEq3O9KZxwun5QbmsxhPascFyDcxVHvNiWKUMq1gIIQ99qfVzs80ch9r5m5e6TWEdAGPaoKDvU_pwNmwEnE-6TnPlN-dOLSAR3LcMGPP610Qxs1X59Do7cTyHJg_0O_Yx9n3Q_-cqAEymwS8EsmM3bwy6yQZBxlXgo72dMNmeD2dDxoxMh4.cIDlywvjcv4MjQeTySSIe9ZPq2r0DlGKNzjQk4pk9UA&dib_tag=se&keywords=slippers&qid=1723685153&sprefix=slippers%2Caps%2C132&sr=8-17&th=1&psc=1",
    "https://www.amazon.com/William-Neuromancer-Collection-Journal-Overdrive/dp/9123588861/ref=sr_1_4?dib=eyJ2IjoiMSJ9.ArlChDCsKlOJy77lHBKtdqgVGLQyBiIWhiuMJDlV78yK4gG4tMY1z1L_LUpfjmHBX6EX5Jk-NsEMlYlSqBGhGeRaQjZE1H6zcxs1Vsilca7wW33gAHr7U1FVV6ltbGW7LLwYp7UKkKy7g4OfZZgMtKtOBabVcrZ0VXcjRgbsub-AdPhnmHgLjTeOOEPm7mmQ_Jq5ZOMYkeyTkTil0_9eXry5K7FPmAXy7FAKQ0QL1_s.X_YmKS6ugBC_hwSFdjMhcEhlp3A87Q8j53DtPNJB744&dib_tag=se&keywords=neuromancer&qid=1723685067&sr=8-4",
    "https://www.amazon.com/HP-Students-Business-Quad-Core-Storage/dp/B0B2D77YB8/ref=sr_1_3?crid=AW0N7J626VW2&dib=eyJ2IjoiMSJ9.DPtOZwisQxLAXAf_kwR_161UU40DqEBUG-Ju057UXaDPU7mvyQL1dQdSw0VcrE9eZjB-FSNBPjs2k3d7nfeqOCqmG7r-GncabSJxAyKjHJ1tef_zILGpDagoX5F0cC1_RiSicVRU_BJYborbOzufN5InS807LFs_9dJAaXMWaReYkt4xwtesWSWed3K2mCOfvh1g0r90D6eZytlkh26xsAVR9oi5ugg6imqIZ4qtjy8.9DtrK2eO0ySrAeMZbTmdVP3PhHpuUfnQiSC9R5G-hxA&dib_tag=se&keywords=laptop&qid=1722726100&sprefix=laptop%2Caps%2C268&sr=8-3&th=1",
    "https://www.amazon.com/Elite-Gourmet-EDB-302BF-Countertop-Temperature/dp/B09RX2WGD3/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=P50rO&content-id=amzn1.sym.352fa4e9-2aa8-47c3-b5ac-8a90ddbece20%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=352fa4e9-2aa8-47c3-b5ac-8a90ddbece20&pf_rd_r=T5W4QKYXP28M7ESMPEPP&pd_rd_wg=cy0Ps&pd_rd_r=c5611503-00e0-4c6e-b622-a66c6a579f4e&pd_rd_i=B09RX2WGD3&th=1"
]

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


def get_product_info():
    products = []

    for item_url in item_list:
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
