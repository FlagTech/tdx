import time
from tdx import TDX

client_id = 'meebox-cc6ed12e-5254-47e3'
client_secret = 'b5bfb7cc-4b43-4f4f-97f8-faaf7705df9b'

tdx = TDX(client_id, client_secret)

# url = 'https://tdx.transportdata.tw/api/basic/v2/Rail/TRA/LiveBoard/Station/1000?$filter=Direction eq 1&$format=JSON'
base_url = "https://tdx.transportdata.tw/api"
# 取得指定[車站]列車即時到離站電子看板(動態前後30分鐘的車次)
endpoint = "/basic/v2/Rail/TRA/LiveBoard/Station/1000"
filter = "Direction%20eq%201"  # 順逆行: [0:'順行', 1:'逆行']
url = f"{base_url}{endpoint}?$filter={filter}&$format=JSON"

stations = tdx.get_json(url)
# print(stations)
for station in stations:
    print(f'{station["StationName"]["Zh_tw"]}->{station["EndingStationName"]["Zh_tw"]}')
time.sleep(3)
print('3 secconds later:')
# 取得指定[車站]列車即時到離站電子看板(動態前後30分鐘的車次)
endpoint = "/basic/v2/Rail/TRA/LiveBoard/Station/4080"
url = f"{base_url}{endpoint}?$filter={filter}&$format=JSON"
stations = tdx.get_json(url)
for station in stations:
    print(f'{station["StationName"]["Zh_tw"]}->{station["EndingStationName"]["Zh_tw"]}')
