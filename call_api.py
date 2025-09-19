from dotenv import load_dotenv
import os
import requests
import pandas as pd
import json

load_dotenv()
API_KEY = os.environ["CWA_API_KEY"]

url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-089"

# api parameter
params = {
    "Authorization": API_KEY,
    "format": "JSON",
    "LocationName": None,
    "ElementName": "溫度,體感溫度,相對濕度,3小時降雨機率",
    "sort": "time"
}

all_loc_name = ["宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣", "臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", "基隆市", "新竹縣", "新竹市", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "嘉義市", "屏東縣"]
correct_loc_name = True

while correct_loc_name:
    LocationName = input("請輸入縣市名稱：")

    if LocationName in all_loc_name:
        correct_loc_name = False
        params["LocationName"] = LocationName
    else:
        print("台灣沒這個縣市，重新輸入啦")
        continue

# call api
reslut = requests.get(url, params=params).json()

# write data into a .json file
# with open("result.json", "w", encoding="utf-8") as f:
#     json.dump(reslut, f, indent=4, ensure_ascii=False)

locations = reslut["records"]["Locations"][0]["Location"]
weatherElement = locations[0]["WeatherElement"]
TTimeSeries = weatherElement[0]["Time"] # 溫度時間佇列
ATTimeSeries = weatherElement[2]["Time"] # 體感溫度時間佇列
RHTimeSeries = weatherElement[1]["Time"] # 相對濕度時間佇列

PoPTimeSeries = weatherElement[3]["Time"] # 3小時降雨機率時間佇列

# all time series
row = []
for t in range(len(TTimeSeries)):
    row.append({
        "Time": TTimeSeries[t]["DataTime"],
        "Temp": TTimeSeries[t]["ElementValue"][0]["Temperature"],
        "AT": ATTimeSeries[t]["ElementValue"][0]["ApparentTemperature"],
        "RH": RHTimeSeries[t]["ElementValue"][0]["RelativeHumidity"]
    })

# PoP time series
PoProw = []
for t in range(len(PoPTimeSeries)):
    PoProw.append({
        "Time": PoPTimeSeries[t]["StartTime"],
        "PoP": PoPTimeSeries[t]["ElementValue"][0]["ProbabilityOfPrecipitation"]
    })

df = pd.DataFrame(row)
df["Time"] = pd.to_datetime(df["Time"]).dt.tz_localize(None)
df = df.set_index("Time")
df = df[df.index.hour % 3 == 0]

PoPdf = pd.DataFrame(PoProw)
PoPdf["Time"] = pd.to_datetime(PoPdf["Time"]).dt.tz_localize(None)
PoPdf = PoPdf.set_index("Time")

df_fianl = df.join(PoPdf, how="left")
print(df_fianl)