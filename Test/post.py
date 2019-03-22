import urllib.request
import os

# os.environ['http_proxy'] = 'http://127.0.0.1:8080'
# os.environ['https_proxy'] = 'https://127.0.0.1:8080'

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
values = {'a': '1'}

data = urllib.parse.urlencode(values).encode('utf-8')
request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request).read().decode('utf-8')
print(response)


