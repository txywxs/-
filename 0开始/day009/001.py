import requests

url = 'https://shuyang.58.com/zufang/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63',
'cookie': 'f=n; commontopbar_new_city_info=5772%7C%E6%B2%AD%E9%98%B3%7Cshuyang; '
          'userid360_xml=38C686A97094CA2CE9675E489E2E33D8; time_create=1608085030574; myLat=""; myLon=""; '
          'id58=OGHdil+x4R+zP06shNMnIA==; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; mcity=shuyang; f=n; '
          'commontopbar_new_city_info=5772%7C%E6%B2%AD%E9%98%B3%7Cshuyang; city=shuyang; 58home=shuyang; '
          'commontopbar_ipcity=shuyang%7C%E6%B2%AD%E9%98%B3%7C0; 58tj_uuid=54fe49fe-556f-4353-9dd5-8831054d5969; '
          'new_uv=1; utm_source=market; init_refer=https%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc'
          '.000000KoW_PGcpxIpMNrn8hS6OUzqw0vjrwnJYkSp_HSoCZ1Zn3vhphykU-fk2EOQknNT-oNf9rOgNKc5DJmGfHZNa7VM3'
          '-LshlBSJnQ2P0lk4m_u4-5Vff9ylJGuRzv_bsD-_fB'
          '-fdrbUO2Fxr9VUeAkhFQg0hZIzUrA_4URMPCamK7aLPBS4PGpZVak_QjI7TWr44U8EJXRATkb2pIpiEA2VbA'
          '.DY_NR2Ar5Od66z3PrrW6ButVvkDj3n-vHwYxw_vU85YIMAQV8qhORGyAp7WIu8L6.TLFWgv'
          '-b5HDkrfK1ThPGujYknHb0THY0IAYqPHWPoQ5Z0ZN1ugFxIZ'
          '-suHYs0A7bgLw4TARqnsKLULFb5HR31pz1ksKzmLmqnfKdThkxpyfqnHRkrHDvrjRYPsKVINqGujYknWTknHbdP0KVgv'
          '-b5HDsPWTLPHbd0AdYTAkxpyfqnHDdn1f0TZuxpyfqn0KGuAnqHbG2RsKWThnqPH6vrHf%2526ck%253D992.2.100.375.147.453.227'
          '.200%2526dt%253D160549302; als=0; new_session=0; wmda_uuid=42d426abe33ea57c8ff92f055cdfb9fe; '
          'wmda_new_uuid=1; wmda_session_id_2385390625025=1605493025485-bc002f11-66a0-53db; '
          'wmda_session_id_11187958619315=1605493028902-fc9f1328-4173-092d; '
          'wmda_visited_projects=%3B2385390625025%3B11187958619315; xxzl_cid=41e473fc781c472aac4805a844da6ec0; '
          'xzuid=d9c57de0-05a4-4a8e-abbc-7f4538804f77; '
          'xxzl_deviceid=ipjHFCdLe3oFygk2DYdTQmMDnULe5u6vFiurHyyte1iNJjM6NK%2FvXX9Ea7sYLDmT '
}

bf = requests.get(url=url,headers=headers)


with open('001.html','w') as a:
    a.write(bf)
