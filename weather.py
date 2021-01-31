import time
import datetime
import requests
from bs4 import BeautifulSoup

# line
def lineNotifyMessage(token, msg):
    headers = {
            "Authorization": "Bearer " + token, 
            "Content-Type" : "application/x-www-form-urlencoded"
    }
	
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

#line token
token = 'your_line_token'

today = str(datetime.date.today())

urls = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-021?Authorization=CWB-DAC435CA-1374-421C-A983-5552AD0B9A3B&locationName=%E5%8D%97%E6%8A%95%E5%B8%82&elementName=WeatherDescription&timeFrom=" + today + "T00%3A00%3A00"
key = "CWB_Key"

r = requests.get(urls, verify=False)
list_of_dicts = r.json()

## the message which you need
message = list_of_dicts['records']['locations'][0]['location'][0]['weatherElement'][0]['time'][0]['startTime']
lineNotifyMessage(token, message)

for i in range(0,4) :
    message = list_of_dicts['records']['locations'][0]['location'][0]['weatherElement'][0]['time'][i]['elementValue'][0]['value']
    lineNotifyMessage(token, message)
    message = list_of_dicts['records']['locations'][0]['location'][0]['weatherElement'][0]['time'][i]['endTime']
    lineNotifyMessage(token, message)
