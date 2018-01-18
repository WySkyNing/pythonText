# -*- coding: utf-8 -*-

#定义一个 list
myList = ["aa","bb","cc"]
print("输出一个 list: %s" %(myList))

size = len(myList)
print("输出 list 的个数: %s" %(size))

print("输出 list 第 0 位的值: %s" %(myList[0]))
print("输出 list 第 1 位的值: %s" %(myList[1]))

print("输出 list 倒数第 1 位的值: %s" %(myList[-1]))
print("输出 list 倒数第 2 位的值: %s" %(myList[-2]))

#ist中追加元素到末尾
print("\n之前的 list:%s" %(myList))

myList.append("11")
print("lst中追加元素到末尾: %s" %(myList))


#lst中下标 1 的位置插入数据
print("\n之前的 list:%s" %(myList))

myList.insert(1,"a1")
print("lst中下标 1 的位置插入数据: %s" %(myList))

#要删除list末尾的元素，用pop()方法：
print("\n之前的 list:%s" %(myList))

myList.pop()
print("删除list末尾的元素:%s" %(myList))

#删除指定位置的元素
print("\n之前的 list:%s" %(myList))

myList.pop(1)
print("删除下标 1 位置的元素: %s" %(myList))

#要把某个元素替换成别的元素，
#可以直接赋值给对应的索引位置：
#list里面的元素的数据类型也可以不同,list元素也可以是另一个list
print("\n之前的 list:%s" %(myList))

aa = ["数据1",11]
myList[2] = aa
print(myList)


#定义一个元组 tuple

#tuple 内的元素指定的地址不能改变,比如里面有一个list 
#不能改为指定其他的list ,但是这个 list 里面的元素是可以改变的

#定义一个普通的 tuple
myTuple = (1,2)

#定义一个只有一个元素额 tuple

# t = (1)  
#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，
#又可以表示数学公式中的小括号，这就产生了歧义，
#因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有1个元素的tuple定义时必须加一个逗号,来消除歧义
t = (1,)

print("输出 tuple: %s,%s" %(myTuple,t))


