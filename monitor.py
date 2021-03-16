from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import smtplib, ssl
import time

smtp_server = "smtp.office365.com"
port = 587
sender_email = "oscar.thorn@outlook.com"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

inet_pages = [
    
]


def check_inet(browser):
    in_stock_products = []
    for page in inet_pages:
        browser.get(page)
        product_stock = browser.find_element_by_xpath(
            "//section[contains(@class, 'product-stock')]/ul[1]/li[1]/label[1]/span[1]")
        if product_stock.text == "I lager":
            in_stock_products.append(page)
    return in_stock_products


def email_products(products):
    # Try to log in to server and send email
    server = smtplib.SMTP(smtp_server, port)
    try:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)

        for product in products:
            print(product)

            message = 'Subject: {}\n\n{}'.format("GPU Available", "Hi,\n{} is available!\nHappy shopping".format(product))

            server.sendmail(sender_email, sender_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


if __name__ == "__main__":
    opts = Options()
    opts.headless = True
    browser = Firefox(options=opts, executable_path=r'C:\\geckodriver\\geckodriver.exe')

    while True:
        time.sleep(60)

        in_stock_products = check_inet(browser)
        email_products(in_stock_products)







