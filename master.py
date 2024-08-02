import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

item = "https://www.amazon.com/ATHMILE-Quick-Dry-Barefoot-Exercise-Accessories/dp/B09Q3MYDQH/?_encoding=UTF8&pd_rd_w=4e3l3&content-id=amzn1.sym.5c57d321-b035-4d54-826c-1342435844f3&pf_rd_p=5c57d321-b035-4d54-826c-1342435844f3&pf_rd_r=D3XMV97P1WNMAJRXPN70&pd_rd_wg=ipopk&pd_rd_r=60972e67-b07a-47bf-8c4e-bcc9f5bbb382&ref_=pd_hp_d_btf_crs_zg_bs_7141123011"

def connect():
    resp = requests.get(item, headers=header)
    if resp.status_code != 200:
        print(resp)
        return None
    return resp

def get_product_title(bs_obj):
    try:
        item_title = bs_obj.find("h1", {"id": "title"}).text.strip()
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

resp = connect()
soup = BeautifulSoup(resp.text, "html.parser").body

rating = get_rating(soup)
print(rating)
