import json
from datetime import date
import requests

from shopeecrawl.getCatIdsShopee import get_category_ids
from lib.mySqlConfig import getsql_insert_into_product, getsql_insert_into_price


def crawl_shopee():
    list_cat_ids = get_category_ids()
    today = date.today();
    day = today.strftime("%b-%d-%Y")
    f_product = open(f"./data/shopee/product-{day}.sql", "a+", encoding="utf-8")
    f_price = open(f"./data/shopee/price-{day}.sql", "a+", encoding="utf-8")
    for cat_id in list_cat_ids:
        newest = 0
        while newest < 8000:
            response = requests.get(f'https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60'
                                    f'&match_id={cat_id}&newest={newest}&order=desc'
                                    f'&page_type=search&scenario=PAGE_OTHERS&version=2')
            data = response.text
            jsondata = json.loads(data)
            for index, item in enumerate(jsondata['items']):
                # insert into product table
                f_product.write(getsql_insert_into_product("shopee", jsondata['items'][index]["item_basic"]["itemid"],
                                                   jsondata['items'][index]["item_basic"]["name"],
                                                   jsondata['items'][index]["item_basic"]["shopid"], cat_id) + ";\n")

                # insert into price table
                f_price.write(getsql_insert_into_price("shopee", jsondata['items'][index]["item_basic"]["itemid"],
                                                 jsondata['items'][index]["item_basic"]["price"],
                                                 jsondata['items'][index]["item_basic"]["item_rating"][
                                                     "rating_star"]) + ";\n")

            newest += 100


if __name__ == '__main__':
    crawl_shopee()
