
def tianqi(city):
	url = 'http://t.weather.sojson.com/api/weather/city/101160101'
	import requests
	res = requests.get(url)
	tq_text = res.text
	import json
	tq_json = json.loads(tq_text)
	wendu = tq_json["data"]["wendu"]
	pm25 = tq_json["data"]["pm25"]
	forecast = tq_json["data"]["forecast"]
	#print(tq_json)
	print(f'{city}:温度{wendu},pm2.5{pm25}')

tianqi(101160101)
