import requests
from lxml import etree
import csv
import re
import time
# //li[@class="cplist"]/a/@href
count = 1
url = "https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.60bf6a152Mspe2&q=tpe&sort=d&style=g&from" \
      "=mallfp..pc_1_searchbutton&type=pc "
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.111 '
                  'Safari/537.36 '
    ,
    'cookie': 'cookie2=1255ffb677a0f3dea0947079fd2941d9; t=5854263382d284f87506f708c36c3a10; '
              '_tb_token_=733e77e397f53; _samesite_flag_=true; cna=KdHdF39NVSgCAXLvMwKvDNQa; xlly_s=1; '
              'sgcookie=E100PBCAZCHBeikYS8A6WvdcVTB5WprelK6tCgz009u18qG6IpIcUwzMidc5zhHd3jABgM%2BH1inRQo6M8oxF5VHjPw'
              '%3D%3D; unb=3244243864; uc3=vt3=F8dCufOGCz8Dm9yJ2sQ%3D&nk2=G5Vaq8Y5OT7ExrY%3D&lg2=W5iHLLyFOGW7aA%3D%3D'
              '&id2=UNJV2TuGwRpuUA%3D%3D; csg=7ddc1abc; lgc=xuanzai5000; cookie17=UNJV2TuGwRpuUA%3D%3D; '
              'dnk=xuanzai5000; skt=c90b66b96fc1a694; existShop=MTYwNDY2NTIzMg%3D%3D; '
              'uc4=id4=0%40UgXSrfwTRDfg5Da0n33bGa%2BQllPn&nk4=0%40GSa%2BQ1QjvEEQk6f%2BCCsV0qXhs30wsw%3D%3D; '
              'tracknick=xuanzai5000; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=043; _nk_=xuanzai5000; '
              'cookie1=Vv1ycvWx2Mu4jG37QtI0SLDqFnSI%2Fq9IK8N55qsDd%2Fo%3D; mt=ci=32_1; thw=cn; '
              'uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie14=Uoe0abRqHNpz2Q%3D%3D'
              '&existShop=false&pas=0&cookie15=URm48syIIVrSKA%3D%3D; '
              'l=eBQ0FRcRO-KcMVpMBO5aFurza77O4IRb8sPzaNbMiInca1PO9FGPgNQVVOPyWdtjgtfbheKyGmkaaRFe8MUdgJdQP8dz9KUMkxJ6'
              '-; tfstk=c2-GBnD8BF71QJ_HPcs6e2DO_0gdZTrVZn-BYHorZUZHDhtFiTzUzXnxK1AMDr1..; '
              'isg=BDo6UF1ZMRBfFL374lND5BhOi2Bc677FjIzLXEQzOU2YN9txLXq_1UoFh8PrpzZd '
}
while True:
    responses = requests.session()
    resp = responses.get(url=url, headers=headers)
    print(resp.content.decode('utf-8'))
    html = etree.HTML(resp.content.decode('utf-8'))
    resp = html.xpath('//p[@class="productTitle"]/a/@title')
    time.sleep(5)
    for i in resp:
        print(i)
        time.sleep(5)