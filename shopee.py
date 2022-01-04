import json

import requests

from lib.mySqlConfig import insert_into_product, insert_into_price

newest = 0
while newest < 100:
    __newest = 60 * newest
    response = requests.get(f'https://shopee.vn/api/v4/search/search_items?by=relevancy&'
                            f'keyword=may%20tinh&limit=60&newest={__newest}'
                            f'&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2')
    data = response.text
    print(newest)
    print(data)
    jsondata = json.loads(data)

    for index, item in enumerate(jsondata['items']):
        # insert into product table
        insert_into_product("shopee", jsondata['items'][index]["item_basic"]["itemid"],
                            jsondata['items'][index]["item_basic"]["name"],
                            jsondata['items'][index]["item_basic"]["shop_location"])

        # insert into price table
        insert_into_price("shopee", jsondata['items'][index]["item_basic"]["itemid"],
                          jsondata['items'][index]["item_basic"]["price"],
                          jsondata['items'][index]["item_basic"]["item_rating"]["rating_star"])

    newest += 1
