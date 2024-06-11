# 转视频流

import requests
import json
import yaml

yaml_file_path = 'passwd.yaml'

# 使用with语句打开文件，确保文件最终会被关闭
with open(yaml_file_path, 'r') as file:
    # 加载YAML文件并将其转换为Python字典
    try:
        data = yaml.safe_load(file)
        
        id_key = data["X-Organization-Key"]
        sn = data["sn"]
    except yaml.YAMLError as exc:
        print(exc)


url = "https://es-flight-api-cn.djigate.com/manage/api/v1.0/stream-converters"

payload = json.dumps({
   "region": "cn",
   "converter_name": "zjtest",
   "sn": sn,
   "camera": "80-0-0",
   "video": "normal-0",
   "idle_timeout": 500,
   "video_quality":0
})
headers = {
   'X-Organization-Key': id_key,
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)