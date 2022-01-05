from lib.mySqlConfig import *
from shopee.shopee import crawl_shopee

if __name__ == '__main__':
    init_database()
    crawl_shopee()