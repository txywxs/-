import requests

if __name__ == "__main__":
    url = "https://movie.douban.com/j/new_search_subjects"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.121 Safari/537.36 '
    }
    param = {
        'sort': 'U',
        'range': '0,10',
        'tags': '',
        'start': '0',
        'countries': '日本'
    }
    response = requests.get(url=url, headers=headers, params=param)
    # 获取响应内容
    print(response.json())