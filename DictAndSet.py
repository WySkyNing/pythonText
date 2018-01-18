# -*- coding: utf-8 -*-


#dict 字典相当于 map 用{}       list []  tuple() 
dictInfo = {"Michael": "95分", "张三": "75分", "Tracy": 85}
print("输出一个字典: %s" % (dictInfo))

print("输出字典中的某个值: %s" % (dictInfo["张三"]))

#覆盖原则
dictInfo["Michael"] = 100
print("改变字典中的某个值: %s" %(dictInfo))

#查询是否有这个 key
print("查询是否有 Tom : %s" % ("Tom" in dictInfo))
print("查询是否有 Tom : %s" % (dictInfo.get("Tom")))
print("查询是否有 Tom : %s" % (dictInfo.get("Tom",-1)))


#添加一个元素
dictInfo["a"] = "33"
print("添加一个 a = 33: %s" %(dictInfo))


#删除一个元素
if "a" in dictInfo:
	dictInfo.pop("a")
	print("删除 a 元素: %s" %(dictInfo))
else:
	print("不存在 a 元素")



#set 和 dict 类似,也是一组 key 的集合,但不存储 value,没有重复的 key,
#要创建一个 set ,需要提供一个 list 作为输入集合
listAge = [1,1,2,3,3,4,5]

#定义的时候别忘了在前面加上 set
#重复元素在 set 中自动被过滤掉
setAge = set(listAge)

print("输出一个 set: %s" % (setAge))

#添加一个元素,重复添加无效果
setAge.add("a")
print("添加一个元素: %s" %(setAge))


#删除一个元素   先判断是否有这个元素
if "a" in setAge:
	setAge.remove("a")
	print("删除一个元素: %s" %(setAge))
else:
	print("setAge 里没有这个元素")


#交集 并集操作
set1 = set([1,2,3,4])
set2 = set([2,3,4,5])
print("输出 set 和 set2 的交集 %s" % (set1 & set2))
print("输出 set 和 set2 的并集 %s" % (set1 | set2))