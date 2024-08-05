import requests
from bs4 import BeautifulSoup
import random
import time

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

items = [
    "https://www.amazon.com/ATHMILE-Quick-Dry-Barefoot-Exercise-Accessories/dp/B09Q3MYDQH/?_encoding=UTF8&pd_rd_w=4e3l3&content-id=amzn1.sym.5c57d321-b035-4d54-826c-1342435844f3&pf_rd_p=5c57d321-b035-4d54-826c-1342435844f3&pf_rd_r=D3XMV97P1WNMAJRXPN70&pd_rd_wg=ipopk&pd_rd_r=60972e67-b07a-47bf-8c4e-bcc9f5bbb382&ref_=pd_hp_d_btf_crs_zg_bs_7141123011",
    "https://www.amazon.com/dp/1624650155/?coliid=IURSU0SKPC6YJ&colid=2F3AW09XJ6Z7S&psc=1&ref_=list_c_wl_gv_ov_lig_pi_dp",
    "https://www.amazon.com/HP-Students-Business-Quad-Core-Storage/dp/B0B2D77YB8/ref=sr_1_3?crid=AW0N7J626VW2&dib=eyJ2IjoiMSJ9.DPtOZwisQxLAXAf_kwR_161UU40DqEBUG-Ju057UXaDPU7mvyQL1dQdSw0VcrE9eZjB-FSNBPjs2k3d7nfeqOCqmG7r-GncabSJxAyKjHJ1tef_zILGpDagoX5F0cC1_RiSicVRU_BJYborbOzufN5InS807LFs_9dJAaXMWaReYkt4xwtesWSWed3K2mCOfvh1g0r90D6eZytlkh26xsAVR9oi5ugg6imqIZ4qtjy8.9DtrK2eO0ySrAeMZbTmdVP3PhHpuUfnQiSC9R5G-hxA&dib_tag=se&keywords=laptop&qid=1722726100&sprefix=laptop%2Caps%2C268&sr=8-3&th=1",
    "https://www.amazon.com/Neuromancer-William-Gibson/dp/0441007465/ref=sr_1_1?crid=369LZU17TQY1T&dib=eyJ2IjoiMSJ9.ArlChDCsKlOJy77lHBKtdqgVGLQyBiIWhiuMJDlV78yK4gG4tMY1z1L_LUpfjmHBX6EX5Jk-NsEMlYlSqBGhGeRaQjZE1H6zcxs1Vsilca7XsCL0Y15IpZE9TsPw3SA7-UPwELkgFje5_GqnW5eVq0D8iEUl6bHrAc7KWwHOBqmHtsou911CX4v5O6yiFoFByMObIuVtYOCQTpX7AtGtGwhUDjsx64_MXwwfpb95QFs.1V3YM80cWLbyiFvAcIR993jEzUNIHTCVA9SKsQsvz7Q&dib_tag=se&keywords=neuromancer&qid=1722726143&sprefix=neuromance%2Caps%2C139&sr=8-1",
]

def connect(url):
    header["User-Agent"] = useragents[random.randrange(len(useragents))]
    resp = requests.get(url, headers=header)
    print(header["User-Agent"])
    if resp.status_code != 200:
        print(resp)
        return None
    
    return resp


def get_product_title(bs_obj):
    try:
        item_title = bs_obj.find("h1", {"id": "title"}).text.strip()
        if len(item_title) > 25:
            item_title = item_title[:25] + "..."
    except:
        item_title = None

    return item_title

def get_price(bs_obj):
    try:
        p = bs_obj.find("span", {"class": "a-price"}).span.text.strip()
    except:
        p=None

    return p

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

def get_info(page):
    obj = {}

    obj["title"] = get_product_title(page)
    obj["image"] = get_image(page)
    obj["price"] = get_price(page)
    obj["rating"] = get_rating(page)

    return obj

def clear_file():
    with open('products.txt', 'w') as f:
        f.write("")


def output_info(obj):
    with open('products.txt', 'a') as f:
        line = ""
        for key in obj:
            line += obj[key] + " "

        f.write(line + '\n')
        f.close()


'''resp = connect(items[0])
soup = BeautifulSoup(resp.text, "html.parser").body
o = get_info(soup)
print(o)'''

while(True):
    print("go")
    for item in items:
        resp = connect(item)
        soup = BeautifulSoup(resp.text, "html.parser").body

        product_info = get_info(soup)
        output_info(product_info)
        time.sleep(random.randrange(6, 30))

    seconds = random.randrange(1800, 2200)
    time.sleep(seconds)
