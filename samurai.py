# restaurants_searcher.py

import json
import csv
import requests
import os #インポート
import sys #インポート

# 初期設定

KEYID = os.environ['keyid']
COUNT = sys.argv[1]
#print(sys.argv)
PREF = sys.argv[2]
FREEWORD = sys.argv[3]
FORMAT = sys.argv[4]


# PARAMS = {"key": myid, "count":sys.argv[0], "large_area":sys.argv[1], "keyword":sys.argv[2], "format":sys.argv[3]}
PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}


def write_data_to_csv(params):
    restaurants = []
    response = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params)
    #print(json_res)
    #リクエストの成功を表すコード200ではない場合、エラー文
    if response.status_code != 200: 
        return("エラーが発生しました")
    response = json.loads(response.text)
    
    # print(type(json_res))
    # print(type(response))
   
    # if "error" in response["results"]:
    #     return print("エラーが発生しました！")
    for restaurant in response["results"]["shop"]:
        restaurant_name = restaurant["name"]
        restaurants.append(restaurant_name)
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(restaurants)
    return print(restaurants)

write_data_to_csv(PARAMS)






