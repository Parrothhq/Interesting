import requests
 
url = 'http://httpbin.org/get'   #目标网址
data = {     #各参数列表（看API网站给了哪些参数）
    'name':'zhangsan',   #name参数赋值
    'age':'25'   #age参数赋值
}
response = requests.get(url,params=data)  #将带参数data的url返回内容保存在response
print(response.url)  #打印url
print(response.text)  #打印返回的内容