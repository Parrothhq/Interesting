import requests
 
url = 'https://www.baidu.com/'  #目标地址
response = requests.get(url)    #将url的返回内容保存在response
print(response.url)  #打印url
print(response.text)  #打印返回的内容