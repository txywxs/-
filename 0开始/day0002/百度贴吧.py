import requests
import bs4

res = r'<div class="d_post_content j_d_post_content clearfix" id=".*" style="display:;">(.*)</div>'
url = "https://tieba.baidu.com/p/7062296961"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
}
content = 1

while True:
    params = {
        'pn': content
    }

    response = requests.get(url=url, headers=headers,params=params)
    bs4_center = bs4.BeautifulSoup(response.text, 'lxml')
    bs4_text = bs4_center.find_all('div', class_='j_d_post_content')
    if content<=5:
        with open('第%s页.txt' % content, 'a',encoding="utf-8") as f:
            for i in bs4_text:
                f.write(i.text+'\n')
        content += 1
        print(url)
        print()
        print()
        print()
        print()
        print()
        url = "https://tieba.baidu.com/p/7062296961?pn=%s"%content
    else:
        print('爬完了')
        break


