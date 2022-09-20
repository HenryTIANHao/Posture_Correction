import requests
import json

url = "https://physical-ai.grate9.com/open/ai/start"

payload = json.dumps({
   "imgs": [
      "https://img.grate9.com/physicalai/ai_hk/2022/0904/6314a223ec211.jpg"
   ],
   "type": 1
})

headers = {
   'openid': 'hk',
   'token': 'B2Stkt4xcmxz1Gpa1p42VHZJLpbW37M3kI2TsnizDqRK3Y3F5ZVvi1smi2gX3TAN',
   'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
