import json
from time import sleep

import requests

from lib.mySqlConfig import getsql_insert_into_price, getsql_insert_into_product
from tiki.getCatIdsTiki import get_category_id, set_browser


def crawl_tiki():
    list_cat_ids = get_category_id()
    f_product = open("./data/tiki/product.sql", "a+", encoding="utf-8")
    f_price = open("./data/tiki/price.sql", "a+", encoding="utf-8")
    for cat_id in list_cat_ids:
        page = 1;
        maxpage = 10;

        while page < maxpage:
            browser = set_browser()
            browser.get(f"https://tiki.vn/api/personalish/v1/blocks/listings"
                        f"?limit=48&aggregations=2&category={cat_id}&page={page}")
            sleep(0.5)
            element = browser.find_element_by_tag_name("body")
            jsondata = json.loads(element.text)
            if maxpage < jsondata["paging"]["last_page"]:
                maxpage = jsondata["paging"]["last_page"]
            for index, item in enumerate(jsondata['data']):
                # insert into product table
                f_product.write(getsql_insert_into_product("tiki", jsondata["data"][index]["id"],
                                                   jsondata["data"][index]["name"],
                                                   jsondata["data"][index]["seller_product_id"], cat_id) + ";\n")

                # insert into price table
                f_price.write(getsql_insert_into_price("tiki", jsondata["data"][index]["id"],
                                                 jsondata["data"][index]["price"],
                                                 jsondata["data"][index]["rating_average"]) + ";\n")
            browser.close()
            page+=1


if __name__ == '__main__':
    crawl_tiki()
