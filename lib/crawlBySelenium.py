from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
SCROLL_PAUSE_TIME = 0.5


def set_browser():
    options = Options()
    options.add_argument("--disable-notifications")
    browser = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
    return browser


def crawl_data():
    browser = set_browser()
    browser.get("https://shopee.vn/shop/267145398/search?page=0&sortBy=pop", browser)
    sleep(SCROLL_PAUSE_TIME)
    # scroll_full_page(browser)
    for i in range(50000):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements = browser.find_elements_by_xpath("//a[contains(@href, 'groups/281334778692054/')]")
    f = open('uid_fb.txt', 'w+')
    lst_uid = []
    for element in elements:
        str_uid = element.get_attribute('href')
        uid = str_uid.replace('https://upload.facebook.com/groups/281334778692054/user/', '')
        uid = uid.replace('/', '')
        if uid not in lst_uid:
            lst_uid.append(uid)
            f.write(uid + '\n')

    sleep(SCROLL_PAUSE_TIME)
    browser.close()


if __name__ == '__main__':
    crawl_data()