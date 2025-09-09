import requests
import pandas as pd

url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-089"
format = "JSON"

# api 參數
params = {
    "Authorization": "CWA-D33FC8AF-31F1-4C17-8D51-0F09FD47A428",
    "limit": 1, 
    "format": "JSON",
    "LocationName": "新北市",
    "ElementName": "溫度", 
    "sort": "time"
}

reslut = requests.get(url, params=params).json()
a = str(reslut["records"]["Locations"][0]["Location"][0]["LocationName"])
print(a)

# 可用的 LocationName 列表
# location_list = ("宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣", "臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", "基隆市", "新竹縣", "新竹市", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "嘉義市", "屏東縣")
# location_list = ("新北市")

# user_input_correct = True

# while user_input_correct:
#     user_input = input("請輸入查詢縣市：")

#     if user_input in location_list:
#         user_input_correct = False
#         params["LocationName"] = user_input
#         result = (requests.get(url, params=params).json()
#         print(result)
#     else:
#         print("請輸入正確的縣市名稱")
