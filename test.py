# 获取组织下的项目列表
import requests
import json

url = "https://es-flight-api-cn.djigate.com/manage/api/v1.0/projects?page=1&page_size=10"

payload = json.dumps({})
headers = {
   'X-Organization-Key': '9d5ed74e9c89e8c2f15656fca2701d82d2007b5a212e6c7feeb69da80b0edcbd',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
