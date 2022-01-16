import requests
from PIL import Image  #使用系统默认图片查看器打开图片的依赖库
url = 'https://api.vvhan.com/api/acgimg'   #目标网址

response = requests.get(url)  #以get方式将url返回内容保存在response
with open("C:\\Users\\parrot\\Desktop\\111.jpg",'wb')as jpg:   #open函数的第一个参数是保存路径；第二个参数是打开文件的模式；“as”后为临时文件参数，给下一行用
    jpg.write(response.content)  

#打开文件操作
img=Image.open('C:\\Users\\parrot\\Desktop\\111.jpg')
img.show()

#完整文件模式：
#t	文本模式 (默认)。
#x	写模式，新建一个文件，如果该文件已存在则会报错。
#b	二进制模式。
#+	打开一个文件进行更新(可读可写)。
#U	通用换行模式（不推荐）。
#r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
#r+	打开一个文件用于读写。文件指针将会放在文件的开头。
#rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
#w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
#w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
#a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
#ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。