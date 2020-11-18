import requests
url = "http://pic.netbian.com/uploads/allimg/190824/212516-15666531161ade.jpg"
r = requests.get(url=url,stream=True)
reponse = int(r.headers.get("Content-Length"))

print("body的数据长度:",reponse)
with open("超级好看的图片.jpg","wb") as fd:
    alls = 0
    for c in r.iter_content(chunk_size=1):
        alls += fd.write(c)
        print("下载进度：%02.2f%%"%(100*alls/reponse))