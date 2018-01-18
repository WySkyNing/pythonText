# -*- coding: utf-8 -*-

def my_abs(x):

	x = int(x)

	#类型检查
	if not isinstance(x,(int,float)):
		raise TypeError("bad type")

	if x >= 0:
		return x
	else:
		return -x

print(my_abs(input("输入一个数,求绝对值")))


#引包
import math

#多个返回值
def move(x,y,setp,angle = 0):
	nx = x + setp * math.cos(angle)
	ny = y - setp * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi / 6)

#但其实这只是一种假象，Python函数返回的仍然是单一值：
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
#而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple
print("多个返回值:  ",x,y)


# n = 2 默认参数 -求 x 的 n 次幂
def power(x,n = 2):

	x = int(x)
	n = int(n)

	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print("平方值 :",power(input("输入一个数,求平方")))
print("多次幂值: ",power(input("输入一个数:求次幂"),input("输入它的次幂")))


#多个默认参数
def student(name,gender,age = 18,city = "HaHa"):
	print("name:",name)
	print("gender: " ,gender)
	print("age: ", age)
	print("city: " ,city)


print("\n四个参数的方法,传了两个参数")
student("tom","man")

print("\n四个参数的方法,传了三个参数,第三个是默认参数")
student("tom","man",20)

print("\n四个参数的方法,city = \"TianJing\" 第三个是默认参数,对应传递给的是方法的第四个参数")
student("tom","man",city = "TianJing")
print("\n")


#Python函数在定义的时候，默认参数L的值就被计算出来了，
#即[]，因为默认参数L也是一个变量，它指向对象[]，
#每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end (L = []):
	print("::",L)
	L.append("END")
	return L
print(add_end())
print(add_end())

#这个问题涉及形参默认值问题，参数默认值是在函数编译compile阶段就已经被确定。
#之后所有的函数调用时，如果参数不显示的给予赋值，那么所谓的参数默认值不过是一个指向那个在compile阶段就已经存在的对象的指针。
#如果调用函数时，没有显示指定传入参数值得话。那么所有这种情况下的该参数都会作为编译时创建的那个对象的一种别名存在。

#如果参数的默认值是一个不可变(Imuttable)数值，那么在函数体内如果修改了该参数，那么参数就会重新指向另一个新的不可变值。
#而如果参数默认值是和本文最开始的举例一样，
#是一个可变对象(Muttable)，那么情况就比较糟糕了。所有函数体内对于该参数的修改，实际上都是对compile阶段就已经确定的那个对象的修改。
def add_end (L = None):
	print("::",L)
	if L is None:
		L = []
	L.append("END")
	return L
print(add_end())
print(add_end())


#可变参数
def calc(*number):
	for x in number:
		print(x)


calc("可变参数:传2个",1,2)
calc("可变参数:传3个",1,2,3)