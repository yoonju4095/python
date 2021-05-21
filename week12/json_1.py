import requests
import json

url = requests.get("https://api.androidhive.info/contacts/")

# JSON 문자열
testData = url.text
print(type(testData)) # str(json 문자열)

data = json.loads(testData)
print(data)
print(type(data))