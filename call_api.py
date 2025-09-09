import requests

def get_url(base_url, api_key, user_input_location):
    return base_url + "?Authorization=" + api_key + "&format=JSON" + "&" + user_input_location

base_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-089"
api_key = "CWA-D33FC8AF-31F1-4C17-8D51-0F09FD47A428"
user_input_location = input("請輸入查詢縣市：")

location_list = ("宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣", "臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", "基隆市", "新竹縣", "新竹市", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "嘉義市", "屏東縣")

user_input_correct = True

while user_input_correct:
    if user_input_location in location_list:
        print(get_url(base_url, api_key))
        user_input_correct = False
    else:
        print("請輸入正確的縣市名稱")
    

