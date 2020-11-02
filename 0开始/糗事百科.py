import re
import os
import requests
import time
urls = 'https://www.qiushibaike.com/imgrank/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 '
                  'Safari/537.36 '
}

resposts = requests.get(url=urls, headers=headers)
resposts_text = resposts.text
res = re.findall('.*?<img src="(.*)" .*>.*?', resposts_text)
for rec in res:
    time.sleep(0.1)
    nums = len(rec)
    if nums > 100:
        try:
            os.mkdir('./糗事')
        except:
            red = rec.split('" ')

            ree = red[0]
            img_url = 'http://'+ree[2:]
            image_data = requests.get(url=img_url, headers=headers).content
            print(type(image_data))
            image_past = re.findall('糗事.*',red[1])

            with open('./糗事/%s.jpg'%image_past[0], 'wb') as fp:
                fp.write(image_data)
else:
