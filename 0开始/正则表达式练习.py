import re

key = "javapythonc++php"
python = re.findall('python', key)[0]

key = "              hello world                 "
hello_world = re.findall('hello world', key)[0]

string = '我喜欢身高为170的女孩'
s170 = re.findall('\d+', string)

key = 'http://www.baidu.com and https://boob.com'
httpss = re.findall('https?://', key)

key = 'lalalahellohahah'  # 输出hello
hello = re.findall('[h]', key)
print(hello)
