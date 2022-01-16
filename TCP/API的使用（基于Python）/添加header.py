import requests
 
url = 'https://www.zhihu.com/'  #目标地址
headers = {   #headers制作
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
response = requests.get(url,headers=headers)     #将带header的url返回内容保存在response
print(response.url)  #打印url
print(response.text)  #打印返回的内容

#有些网站，如果不加header会报错（如：知乎），“An internal server error occured.”，所以要加一个headers，如果想访问就必须得加headers信息
#https://blog.csdn.net/xc_zhou/article/details/81021496