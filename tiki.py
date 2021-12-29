import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SCROLL_PAUSE_TIME = 0.5


def set_browser():
    options = Options()
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver", chrome_options=options)
    return browser


if __name__ == '__main__':
    browser = set_browser()
    browser.get("https://tiki.vn/api/v2/products?limit=48&include=advertisement&aggregations=2&"
                "trackity_id=5d52ce02-5821-bcaf-7a2a-064cdf911585&q=laptop%20asus"
                "&fbclid=IwAR0r5P2JzQLnhNsTaJauNwkjL957M5qa9SkATCQnYiNpgOFK40EP__nOT00")
    sleep(1)
    element = browser.find_element_by_tag_name("body")
    jsondata = json.loads(element.text)
    jsonobject = json.dumps(jsondata)
    f = open("tiki.json", "w+")
    f.write(jsonobject)
    f.close()

    print(jsondata)

    browser.close()
