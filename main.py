from time import sleep
from shopee.shopee import crawl_shopee
from tiki.tiki import crawl_tiki

if __name__ == '__main__':
    while 1:
        # try:
        #     crawl_tiki()
        # except Exception as err:
        #     print(Exception, err)

        try:
            crawl_shopee()
        except Exception as err:
            print(Exception, err)
        sleep(3*60*60)
