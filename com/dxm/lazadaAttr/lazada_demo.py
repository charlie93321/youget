import json

import lazop


url=''

app_key=''
app_secret=''
appkey =app_key
appSecret=app_secret

client = lazop.LazopClient('https://api.lazada.vn/rest',appkey,appSecret)
request = lazop.LazopRequest('/category/attributes/get','GET')
request.add_api_param('primary_category_id', '6396')
response = client.execute(request)
print(response.type)
print(json.dumps(response.body,ensure_ascii=False))


