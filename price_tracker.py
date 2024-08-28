import web_scraper
import csv
import smtplib
import time
import random


def send_email(discount_list):
    email = "marcod082@gmail.com"
    receiver = "marcod082@gmail.com"

    subject = "Amazon Discount alert"
    body = ""
    for item in discount_list:
        body += f"{item['title']} - ${item['price']} - {item['rating']}\n{item['url']}\n\n"
        
    text = f"subject: {subject}\n\n{body}"
    server = smtplib.SMTP("smtp.gmail.com", 587) 
    server.starttls()

    server.login(email, "")
    server.sendmail(email, receiver, text)


def get_discount(master_price, current_price):
    discount_inverse = current_price/master_price
    discount = (1 - discount_inverse) * 100
    
    return discount

#places items in either discounted or nondiscounted lists by comparing master price with current price
def get_discounted_products(current_products):
    discounted_products = []
    nonDiscount_products = []
    with open("product_info.csv","r") as csv_file:
        product_index = 0

        csv_reader = csv.DictReader(csv_file)
        for master_product in csv_reader:
            current_product = current_products[product_index]

            try:
                master_price = float(master_product["price"])
                current_price = float(current_product["price"])
                if get_discount(master_price, current_price) > 10.0:
                    discounted_products += [current_product]
                else:
                    nonDiscount_products += [current_product]
            except:
                print(f"current product price is none")

            product_index += 1

    return discounted_products, nonDiscount_products


if __name__ == "__main__":

    while(True):
        current_products = web_scraper.get_product_info()
        discount_list, nonDiscount_list = get_discounted_products(current_products)
    
        #update csv file and send email if either list has elements
        if len(discount_list) > 0: 
            send_email(discount_list)
            web_scraper.clear_csv()
            web_scraper.output_csv(nonDiscount_list) #if discount_list has items then num of nonDiscount items has changed and csv must be updated
        time.sleep(random.randrange(7200, 9000)) #wait 2-2.5 hours before checking current prices
