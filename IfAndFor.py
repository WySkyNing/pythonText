#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
age = input("请输入你的年龄")

age = int(age)

if age < 18:
	print("你还没有成年")
elif age < 30:
	print("你还没到中年")
else:
	print("你已经老了")


#for...in循环
l = [1,2,3,4]
for _l in l:
  	print("使用 for...in 循环： %s " %(_l)) 

#range()函数，可以生成一个整数序列（从 0 开始，整数），再通过list()函数可以转换为list
myList = list(range(101))

#有
sum = 0
for x in range(1,10):
	sum = sum + x
print("使用 for x in ... 循环 定义起始和结束： %s " %(sum)) 


sum1 = 0
for x in myList:
	sum1 = sum1 + x
print("使用 for x in ... 循环 参数为 list： %s " %(sum1)) 


#while 循环
sum2 = 0;
while sum2 < 10:
	sum2 = sum2 +2
	print("while 循环 输出 sum2 %s" % (sum2))


#break  跳出整个循环
sum3 = 0;
while sum3 < 10:
	sum3 = sum3 +2
	if sum3 == 6:
		break
	print("while 循环 sum3 等于 6 时 break %s" % (sum3))


#continue 跳出本次循环
sum4 = 0;
while sum4 < 10:
	sum4 = sum4 + 2
	if sum4 == 6:
		continue
	print("while 循环 sum4 等于 6 时 continue %s" % (sum4))