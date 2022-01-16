from jsonpath import jsonpath  #用于寻找json里面指定变量的库
import requests
import json
import re  #去除指定字符串的库
 
url = 'https://api.vvhan.com/api/weather'   #目标网址
data = {     #各参数列表（看API网站给了哪些参数）
    'city':'深圳'
}
response = requests.get(url,params=data)  #将带参数data的url返回内容保存在response
dat = json.loads(response.text)  #将返回内容格式化为json
PrettyText = json.dumps(dat, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)  #将json格式化为“更具立体感”的字符串（带多个回车）

#取出返回结果的指定变量
city = jsonpath(dat, "$..city")   #取出返回结果中的“city”变量值
type = jsonpath(dat, "$..type")   #取出返回结果中的“type”变量值
tip = jsonpath(dat, "$..tip")   #取出返回结果中的“tip”变量值

#句子拼接
hello = "早上好！今天"+str(city)+"的天气："+str(type)+'\n'+"鹦鹉先生提醒您：" + str(tip)   #字符串拼接（记得要将取出来的变量值强制转换为str）
hello1 = re.sub('[][\']', '', hello)  #使用re库的sub函数：去除]['字符，替换为（空），目标字符串为hello，将结果存到hello1

#测试结果
print(hello1)
print(PrettyText)

result = ''
for i in response.json()['info']:
    result+=i['v']+'\n'
print(result)