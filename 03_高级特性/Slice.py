# -*- coding : uft-8 -*-

#切片 #tuple 和 str 也适用
L = list(range(100))

print("截取下标 0 到 10 : ", L[:10])

print("截取下标 10 到 20 : ", L[10:20])

print("截取下标 倒数第十位 到最后一位: ", L[-10:])

print("所有数每五个取一个: " , L[::5])

print("前十个数每两个取一个: ",L[:10:2])






#迭代 -相当于 遍历

L1 = list(range(10))

print("\n迭代list")
for x in L1:
	print(x)

D1 = {"a":1,"b":2,"c":3,"d":4}
print("\n迭代 dict,默认输出的是 Key")
for k in D1:
	print(x)


print("\n迭代 dict 的 value")
for v in D1.values():
	print(x)
	

print("\n同时0迭代 dict 的 key 和 value")
for k,v in D1.items():
	print(k,v)


print("\n迭代字符串")
_str = "ABCD"
for s in _str:
	print(s)


#判断对象是否可以迭代  collections- 收藏  Iterable-可迭代的
from collections import Iterable

print("str 是否可以被迭代: " , isinstance("abc",Iterable))
print("lis 是否可以被迭代: ", isinstance(L1,Iterable))
print("整数是否可以被迭代: ",isinstance(123,Iterable))


print("\n对list实现类似Java那样的下标循环")
for i,value in enumerate (L1):
	print(i,value)



#列表生成式 
#- for前面是要生成的 list 的 item, for 后是给前面的 x 赋值  range 生成一个 list
#  还可加上判断 真特么强

_list1 = [x * x for x in range(1,11) if x % 2 == 0]
print(_list1)

#还可以是用双层循环
_list2 = [x + n for x in ["A","B","C"] for n in ["a","b","c"]]
print(_list2)

#int 和 str 不能相加
_list3 = [x + n for x in {"A":"1","B":"2"}.values() for n in ["a","b","c"]]
print(_list3)


#列出当前目录下的所有文件夹
import os

print("\n列出当前目录下的所有文件夹:")
print([d for d in os.listdir(".")])


#把 list 中的 item 变成小写
_list4 = ["A","B","C"]
print("\n把 list 中的 item 变成小写")
print([s.lower() for s in _list4])

#输出的是一个对象 - 一个生成器
print(s.lower() for s in _list4)



#生成器

#列表元素按照某种算法推算出来
#可以在循环的过程中不断推算出后续的元素,这样就不必创建完整的list
#从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

#新建生成器 方法一
#直接把 lsit 的 [] 改成 ()
_generator1 = (x for x in range(5))
print("输出生成器中的值(迭代法): ")
for x in _generator1:
	print(x)



#generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print("\n自己创建生成器: ")
def fib(max):

	n ,a ,b = 0,0,1

	while n < max:

		yield b

		a , b = b , a + b
		n = n + 1

	return "done"

for x in fib(6):
	print(x)
		
	
