import bs4
import requests
import re,os
url = 'https://www.souutu.com/mnmm/mote/16925.html'
rest = r"\d/(\d{1,2})"
url = url
res = requests.get(url=url)
bs = bs4.BeautifulSoup(res.text, 'lxml')
bs_img = bs.find_all('img', id="showpicsouutuIs2020")
bs_a = bs.find_all('a', class_="Nnext imgpage-right")
bs_page = bs.find('div', class_="showcenter")
cont = 0
bs_page_max = bs_page.text
bs_page_max = int(re.findall(rest, bs_page_max)[0])

bs_img_src = bs_img[0]['src']
bs_img_alt = bs_img[0]['alt']
bs_a_right_href = bs_a[0]['href']
os.mkdir("./%s" % bs_img_alt)
with open('./%s/%s.jpg' % (bs_img_alt, cont), 'wb') as f:
    bc = requests.get(str(bs_img_src))
    f.write(bc.content)
    url = bs_a_right_href
