import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lib.mySqlConfig import insert_into_price, insert_into_product

SCROLL_PAUSE_TIME = 0.5


def set_browser():
    options = Options()
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path="../chromedriver_win32/chromedriver", chrome_options=options)
    return browser


if __name__ == '__main__':
    browser = set_browser()
    browser.get("https://x.o-s.io/sda?a_slot=top&a_type=product&cli_ubid=a0b22cc7-0ca4-4eb3-ba53-b91e6e861594"
                "&client_id=18662&country=VN&currency=VND&keywords%5B0%5D=may%20tinh"
                "&language=vi&page_type=SEARCH&pcnt=30")
    sleep(1)
    element = browser.find_element_by_tag_name("body")
    jsondata = json.loads(element.text)

    print(jsondata)

    for index, item in enumerate(jsondata['products']):
        # insert into product table
        insert_into_product("sendo", jsondata['products'][index]['skuId'],
                            jsondata['products'][index]['name'],
                            jsondata['products'][index]['sellerId'])

        # insert into price table
        insert_into_price("sendo", jsondata['products'][index]['skuId'],
                          jsondata['products'][index]['salePrice'],
                          jsondata['products'][index]['score'])

    browser.close()
