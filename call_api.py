import requests
import pandas as pd
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["CWA_API_KEY"]

url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-089"

# api parameter
params = {
    "Authorization": API_KEY,
    # "limit": 1,
    "format": "JSON",
    "LocationName": "新北市",
    "ElementName": "溫度,體感溫度",
    "sort": "time"
}

# call api
reslut = requests.get(url, params=params).json()

try:
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(reslut, f, ensure_ascii=False, indent=4)
except:
    pass


# city name
LocationName = str(reslut["records"]["Locations"][0]["Location"][0]["LocationName"])
print(LocationName)

location = reslut["records"]["Locations"][0]["Location"][0] # 新北市
elements = location["WeatherElement"]

# create element list for column name
elementList = []
for i in range(len(elements)):
    elementName = elements[i]["ElementName"]
    elementList.append(elementName)
print(elementList)


# time quntity
timeNumber = len(elements[0]["Time"])

# create time list for row name
timeList = []
for i in range(timeNumber):
    eachTime = elements[0]["Time"][i]["DataTime"]
    timeList.append(eachTime)
print(timeList)


# create Temperature, ApparentTemperature list
tempList = []
appTempList = []

# append value to tempList, appTempList
for i in range(timeNumber):
    tempValue = elements[0]["Time"][i]["ElementValue"][0]["Temperature"]
    tempList.append(tempValue)

    appTempValue = elements[1]["Time"][i]["ElementValue"][0]["ApparentTemperature"]
    appTempList.append(appTempValue)

print(tempList)
print(appTempList)