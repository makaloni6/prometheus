import requests
import json 

url = 'http://localhost:9090/api/v1/targets'

def get_targets():
    response = requests.get(url)
    items = json.loads(response.text)

    for item in items['data']['activeTargets']:
        for k, v in item.items():
            print(k, v)