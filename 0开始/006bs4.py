from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./爬取的源代码/baidu.html'), 'lxml')
soup = soup.find_all(['div', 'a'], limit=1)
print(soup)
