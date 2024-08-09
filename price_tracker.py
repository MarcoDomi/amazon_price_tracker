import web_scraper
import csv

# TODO compare price in e/ object to e/ respective price in csv file to find discount
# TODO if discount is at least 10% then send email

def calculate_discount(master_price, current_price):
    discount_inverse = current_price/master_price
    discount = (1 - discount_inverse) * 100
    return discount


def get_discounted_products(current_products):
    discounted_items = []
    with open("product_info.csv","r") as csv_file:
        product_index = 0
        
        csv_reader = csv.DictReader(csv_file)
        for master_product in csv_reader:
            current_product = current_products[product_index]
            master_price = float(master_product["price"])
            current_price = float(current_product["price"])
           
           
            product_index += 1
            

if __name__ == "__main__":
    #current_products = web_scraper.get_product_info()
    temp = [{"price": "17.75"}, {"price": "17.29"}, {"price": " 269.99"}, {"price": "11.19"}]
    get_discounted_products(temp)
