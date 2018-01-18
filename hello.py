#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：

print("hello python")
print(300 + 600)
name = input("请输入你的名字")
name
print(name)

#与
print(True and False)
#或
print(True or False)
#非
print(not False)

age = 18;
if age > 3:
	print("a")
else:
	print("b")
	
#有余数
print(10 / 3)
#取整
print(10 // 3)


#返回对应的 ASCII 数值，或者 Unicode 数值 数值都是十进制的
print("输出 a 的 ASCII 值:  %s" % (ord("a")))

print("输出 中 的 Unicode值: %s" % (ord("中")))

print("输出 ASCCII 66 对应的值: %s" % (chr(66)))

print("输出 25991 对应的 Unicode 值: %s" % (chr(25991)))

#字符串对应的十六进制写法
print("输出 中文 的 16 进制写法: %s" % ("\u4e2d\u6587"))




#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，
#或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

#编码

by1 = "ABC".encode("ascii") 
print("输出把 ABC 转换成 bytes 类型: %s" % (by1))

#汉字没有对应的 ASCII
by2 = "中文".encode("utf-8")
print("输出把 中文 转换成 bytes 类型: %s" % (by2))



#解码
str1 = b"ABC".decode("ASCII")
print("输出把 b\"ABC\" 转换成字符串: %s" % (str1))

str2 = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print("输出把 b'\xe4\xb8\xad\xe6\x96\x87' 转换成字符串: %s" % (str2))

str3 = b'\xe4\xb8\xad\xf6'.decode('utf-8',errors = "ignore")
print("输出把 b'\xe4\xb8\xad\xf6' 转换成字符串(忽略转换过程中一小部分无效字节): %s" % (str3))






