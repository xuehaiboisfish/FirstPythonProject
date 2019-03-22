import requests
import json
import uuid

def loginGetToken():

    url = 'http://localhost:8080/ship-manage/login'

    request_header = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

    request_param = {'name': 'admin', 'pass': '123123'}

    # response = requests.post(url, data=json.dumps(request_param), headers=request_header)
    #
    # print(response.json())

    sss = requests.session()
    response = sss.post(url, data=json.dumps(request_param), headers=request_header)
    print(response.json())

    return response.json()['data']['token']


token = loginGetToken()



url = 'http://localhost:8080/ship-manage/ship/component/shipComponent'
request_header = {
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

request_param = {
    'checkCode': '',
    'componentCategoryId': '',
    'componentId' : str(uuid.uuid1()),
    'componentCname': '1',
    'componentCode': '',
    'componentEname': '',
    'componentModel': '2',
    'componentNumber': '',
    'componentProductId': '',
    'componentStatus': '1',
    'componentType_id': 'E25F1252-577F-44B8-B280-6A60C62504E0',
    'componentTypeid': 'E25F1252-577F-44B8-B280-6A60C62504E0',
    'cwbtCode': 'KP-300-000-000',
    'installationSite': '',
    'isForeign': '',
    'lastRepairDate': '',
    'manufacturer': '3',
    'origin': '',
    'parameter': '',
    'parentId': '1EA682E9-B2E0-47B6-98E9-8AB37B88C3AF',
    'post_id': '413936AB-970D-4CFB-B05C-BA88F4C869E0',
    'postid': '413936AB-970D-4CFB-B05C-BA88F4C869E0',
    'produceDate': '',
    'remark': '',
    'reorder': '',
    'riskLevel': '3',
    'runingRate': '',
    'shipId': '28FF3294-D7C8-4EDD-8DD1-BC0C58003400',
    'sortId': '',
    'totalMeter': '',
    'companyId' : 'EC56DC39-5312-4627-BEEE-5A47D3BAEE98'
}

ss = requests.session()
response = ss.post(url, data=json.dumps(request_param), headers=request_header)

print(response.status_code)
print(response.text)


