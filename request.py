import requests

url = "https://physical-ai.grate9.com/open/ai/result"

payload = {}
files = [

]

headers = {
    'token': 'hk',
    'openid': 'B2Stkt4xcmxz1Gpa1p42VHZJLpbW37M3kI2TsnizDqRK3Y3F5ZVvi1smi2gX3TAN',
    'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
