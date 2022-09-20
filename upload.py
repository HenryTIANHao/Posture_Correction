import requests

url = "https://physical-ai.grate9.com/open/common/uploadImg"

payload = {}
files = [
    ('file', ('D:/LI/left.jpg', open('D:/LI/left.jpg', 'rb'), 'image/jpeg'))
]

headers = {
    'openid': 'hk',
    'token': 'B2Stkt4xcmxz1Gpa1p42VHZJLpbW37M3kI2TsnizDqRK3Y3F5ZVvi1smi2gX3TAN',
    'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
