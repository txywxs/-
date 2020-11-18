import re
import requests

rec = r'<span class="item-title weight-bold ellipsis-2">(.*?)</span>'
url = "https://www.36kr.com/"
headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/13.0.3 Mobile/15E148 Safari/604.1 '
}
responses = requests.get(url=url, headers=headers)

res = responses.content.decode()

b = re.findall(rec, res)
for i in b:
    print(i)
