import time
import os
from tdx import TDX

client_id = os.getenv('TDX_ID')
client_secret = os.getenv('TDX_SECRET')

tdx_client = TDX(client_id, client_secret)

# url = 'https://tdx.transportdata.tw/api/basic/v2/Rail/TRA/LiveBoard/Station/1000?$filter=Direction eq 1&$format=JSON'
base_url = "https://tdx.transportdata.tw/api"
# 取得指定[車站]列車即時到離站電子看板 (動態前後 30 分鐘的車次)
endpoint = "/basic/v2/Rail/TRA/LiveBoard/Station/1000"
# MicroPython 的 get 不會自動 urlencode, 要自己做
# https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding
filter = "Direction%20eq%201"  # 順逆行: [0:'順行', 1:'逆行']
url = f"{base_url}{endpoint}?$filter={filter}&$format=JSON"

stations = tdx_client.get_json(url)
# print(stations)
for station in stations:
    print(f'{station["StationName"]["Zh_tw"]}->{station["EndingStationName"]["Zh_tw"]}')
time.sleep(3)
print('3 secconds later:')
# 3 後改以嘉義車站查詢, 測試不需重新索取 token
endpoint = "/basic/v2/Rail/TRA/LiveBoard/Station/4080"
url = f"{base_url}{endpoint}?$filter={filter}&$format=JSON"
stations = tdx_client.get_json(url)
for station in stations:
    print(f'{station["StationName"]["Zh_tw"]}->{station["EndingStationName"]["Zh_tw"]}')
