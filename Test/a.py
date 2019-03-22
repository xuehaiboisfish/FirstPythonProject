# list = ['a', 1, 'c']
# print(list)
#
# obj = ('aa', 'bb')
# print(obj)
#
# dic = {'a': 1, 'b': 2}
# print(dic.keys())
# print(dic.values())
#
# cnt = 0
# while cnt < 5:
#     print(cnt)
#     cnt += 1
# else:
#     print(cnt)
#
# for num in range(0, 50, 10):
#     print(num)
#
# x=1
# print('D:\\pictures\%s.jpg'%x)

import urllib.request
import re
import requests

url='http://localhost:8080/ship-manage/login'
headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36'}

#获取token
sss = requests.Session()
# r = sss.get(url, headers = headers)
# print(r.content.decode('utf-8'))
# reg = r'loginToken'
# pattern = re.compile(reg)
#
# result = pattern.findall(r.content)
# print(result)


data = {
    '__token__' : '',
    'user': 'admin',
    'pass': '123123'
}

#登录后
r = sss.post(url, data, headers)
print(r.content.decode('utf-8'))

