# 停止流转码
import requests

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


url = "https://es-flight-api-cn.djigate.com/manage/api/v1.0/stream-converters/06595A62A74769BD812669912D2FFCFC"

payload={}
headers = {
   'X-Organization-Key': id_key,
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)