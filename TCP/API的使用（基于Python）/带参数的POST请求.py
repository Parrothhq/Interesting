import requests
 
url = 'http://httpbin.org/post'  #目标网址
data = {   #参数列表
    'name':'jack',
    'age':'23'
    }
response = requests.post(url,data=data)  #将带参数data的url返回内容保存在response
print(response.url)  #打印url
print(response.text)  #打印返回的内容