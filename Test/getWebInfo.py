import urllib.request
import re

def login(login_url = 'http://****.com/users/sign_in', username='', password=''):

    #请求头
    my_headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
    }

    #获取token
    sss = urllib.request.session
    r = sss.get(login_url, headers = my_headers)
    reg = r'<input name="authenticity_token" type="hidden" value="(.*)" />'
    pattern = re.compile(reg)
    result = pattern.findall(r.content)
    token = result[0]

    #postdata
    my_data = {
        'commit' : '登录',
        'utf8' : '%E2%9C%93',
        'authenticity_token' : token,
        'user[email]': username,
        'user[password]':password
    }

    #登录后
    r = sss.post(login_url, headers = my_headers, data = my_data)
    return sss


