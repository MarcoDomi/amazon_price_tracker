import web_scraper
import csv
import smtplib


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

    server.login(email, "nnxx zmwe kdft qkpv")
    server.sendmail(email, receiver, text)


def get_discount(master_price, current_price):
    discount_inverse = current_price/master_price
    discount = (1 - discount_inverse) * 100
    
    return discount


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
    # current_products = web_scraper.get_product_info()
    # discount_list = get_discounted_products(current_products)

    test_scraped_data = [
        {
            "title": "item1",
            "price": "21.75",
            "rating": "4.5",
            "url": "https://www.amazon.com/dp/1646091809/?coliid=I1R9351T70G1BR&colid=2F3AW09XJ6Z7S&psc=1&ref_=_sed_dp",
        },
        {
            "title": "item2",
            "price": "39.29",
            "rating": "3.5",
            "url": "https://www.amazon.com/dp/1624650155/?coliid=IURSU0SKPC6YJ&colid=2F3AW09XJ6Z7S&psc=1&ref_=list_c_wl_gv_ov_lig_pi_dp",
        },
        {
            "title": "item3",
            "price": "234.99",
            "rating": "4.8",
            "url": "https://www.amazon.com/HP-Students-Business-Quad-Core-Storage/dp/B0B2D77YB8/ref=sr_1_3?crid=AW0N7J626VW2&dib=eyJ2IjoiMSJ9.DPtOZwisQxLAXAf_kwR_161UU40DqEBUG-Ju057UXaDPU7mvyQL1dQdSw0VcrE9eZjB-FSNBPjs2k3d7nfeqOCqmG7r-GncabSJxAyKjHJ1tef_zILGpDagoX5F0cC1_RiSicVRU_BJYborbOzufN5InS807LFs_9dJAaXMWaReYkt4xwtesWSWed3K2mCOfvh1g0r90D6eZytlkh26xsAVR9oi5ugg6imqIZ4qtjy8.9DtrK2eO0ySrAeMZbTmdVP3PhHpuUfnQiSC9R5G-hxA&dib_tag=se&keywords=laptop&qid=1722726100&sprefix=laptop%2Caps%2C268&sr=8-3&th=1",
        },
        {
            "title": "item4",
            "price": "34.19",
            "rating": "3.8",
            "url": "https://www.amazon.com/Neuromancer-William-Gibson/dp/0441007465/ref=sr_1_1?crid=369LZU17TQY1T&dib=eyJ2IjoiMSJ9.ArlChDCsKlOJy77lHBKtdqgVGLQyBiIWhiuMJDlV78yK4gG4tMY1z1L_LUpfjmHBX6EX5Jk-NsEMlYlSqBGhGeRaQjZE1H6zcxs1Vsilca7XsCL0Y15IpZE9TsPw3SA7-UPwELkgFje5_GqnW5eVq0D8iEUl6bHrAc7KWwHOBqmHtsou911CX4v5O6yiFoFByMObIuVtYOCQTpX7AtGtGwhUDjsx64_MXwwfpb95QFs.1V3YM80cWLbyiFvAcIR993jEzUNIHTCVA9SKsQsvz7Q&dib_tag=se&keywords=neuromancer&qid=1722726143&sprefix=neuromance%2Caps%2C139&sr=8-1",
        },
    ]
    discount_list,nonDiscount_list = get_discounted_products(test_scraped_data)
    print(len(discount_list))
    print(len(nonDiscount_list))

    if len(nonDiscount_list) > 0:
        web_scraper.clear_csv()
        web_scraper.output_csv(nonDiscount_list)

    if len(discount_list) > 0:
        send_email(discount_list)
