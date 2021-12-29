import requests
import json

response = requests.get('https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword=may%20tinh&limit=60&newest'
                        '=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2')
data = response.text
jsondata = json.loads(data)

for index, item in enumerate(jsondata['items']):
    print(index,
    jsondata['items'][index]["item_basic"]["item_rating"]["rating_star"])
# print(jsondata['items'][24]["item_basic"]["name"])