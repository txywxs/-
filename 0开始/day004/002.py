import json
import requests
url = "https://webapi.qingting.fm/api/mobile/rank"
headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/13.0.3 Mobile/15E148 Safari/604.1 '
}

responses = requests.get(url=url, headers=headers)

res = responses.content.decode()

print(type(res))

json_dict = json.loads(res)

print(type(json_dict))






for i in json_dict.get("rankinglist"):
    print(i.get('title'),i.get('playCount'))