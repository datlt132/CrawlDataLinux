import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lib.mySqlConfig import insert_into_product, insert_into_price

SCROLL_PAUSE_TIME = 0.5


def set_browser():
    options = Options()
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver", chrome_options=options)
    return browser


if __name__ == '__main__':
    agg = 2;
    while agg < 10:
        browser = set_browser()
        browser.get(f"https://tiki.vn/api/v2/products?limit=48&include=advertisement&aggregations={agg}&"
                    "trackity_id=5d52ce02-5821-bcaf-7a2a-064cdf911585&q=laptop%20asus"
                    "&fbclid=IwAR0r5P2JzQLnhNsTaJauNwkjL957M5qa9SkATCQnYiNpgOFK40EP__nOT00")
        sleep(1)
        element = browser.find_element_by_tag_name("body")
        jsondata = json.loads(element.text)

        print(jsondata)

        for index, item in enumerate(jsondata['data']):
            # insert into product table
            insert_into_product("tiki", jsondata['data'][index]["id"],
                                jsondata['data'][index]["name"],
                                jsondata['data'][index]["sku"])

            # insert into price table
            insert_into_price("tiki", jsondata['data'][index]["id"],
                              jsondata['data'][index]["price"],
                              jsondata['data'][index]["rating_average"])

        browser.close()
        agg += 1
