import json

import requests


def get_category_ids():
    listid = []
    response = requests.get("https://shopee.vn/api/v4/pages/get_category_tree")
    data = response.text
    item = json.loads(data)

    for index, category in enumerate(item["data"]["category_list"]):
        # print(index)
        # print(item["data"]["category_list"][index]["catid"])
        # print(item["data"]["category_list"][index]["name"])
        listid.append(item["data"]["category_list"][index]["catid"])

    print(listid)
    return listid


if __name__ == '__main__':
    get_category_ids()