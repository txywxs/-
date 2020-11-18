import requests
import json
url = "https://m.lagou.com/listmore.json?pageNo=1&pageSize=15"
headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/13.0.3 Mobile/15E148 Safari/604.1 '
}

responses = requests.get(url=url, headers=headers)


res = responses.content.decode()

json_dict = json.loads(res)

print(type(json_dict))

print(json_dict.get("content"))
