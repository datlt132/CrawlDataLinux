import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_browser():
    options = Options()
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver", chrome_options=options)
    return browser


def get_category_id():
    browser = set_browser()
    browser.get("https://tiki.vn/api/personalish/v1/blocks/categories"
                "?block_code=featured_categories&trackity_id=000362b0-1eec-ae51-bb7e-94c9812f29db")
    sleep(0.5)
    list_id = []
    element = browser.find_element_by_tag_name("body")
    item = json.loads(element.text)
    browser.close()

    for index, category in enumerate(item["items"]):
        list_id.append(item["items"][index]["id"])

    print(list_id)
    return list_id


if __name__ == '__main__':
    get_category_id()