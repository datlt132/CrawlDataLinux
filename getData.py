import json
from lib.mySqlConfig import *

def GetProduct(jsondata):
    for index, item in enumerate(jsondata['items']):
        # insert into product table
        insert_into_product(jsondata['items'][index]["item_basic"]["name"],
        jsondata['items'][index]["item_basic"]["shop_location"])
        
        # insert into price table
        insert_into_price(jsondata['items'][index]["item_basic"]["itemid"],
        jsondata['items'][index]["item_basic"]["price"], 
        jsondata['items'][index]["item_basic"]["item_rating"]["rating_star"])
