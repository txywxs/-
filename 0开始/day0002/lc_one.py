import requests
import re

url = 'http://www.biquge.info/32_32050/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
responst = requests.get(url=url, headers=headers)
print(responst.text)
