from time import sleep

from lib.mySqlConfig import *
from shopeecrawl.shopee import crawl_shopee
from tiki.tiki import crawl_tiki
from lib.mySqlConfig import execute_sql_statement_from_file

if __name__ == '__main__':
    init_database()
    while 1:
        # try:
        #     crawl_tiki()
        # except Exception as err:
        #     print(Exception, err)
        # execute_sql_statement_from_file("./data/tiki/price.sql")

        try:
            crawl_shopee()
        except Exception as err:
            print(Exception, err)
        sleep(3*60*60)
