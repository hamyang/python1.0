
# set集合类型

'''
+ set集合是一个 无序且元素不重复的 集合的数据类型
+set集合所有 中括号或者set()方法来定义
'''

#集合的定义方式
vars = {1,2,3,'a','b',1}
print(vars,type(vars))

#如果需要定义一个空集合时 只能使用 set()方法
vars = set('123456')
print(vars,type(vars))
vars = set()
print(vars)

a = {1, 2, 3, 'a'}
#给集合添加元素
a.add('c')
#无法获取集合中的单个元素（因为无序），但是可以添加和删除
print(a.discard('a'))
print(a)
#检查当前的元素是否在集合中
print(2 in a)


# 集合主要用于运算,交集，差集，并集，对称集合
a = {1,2,3,'a','b'}
b = {1,'a',22,33}

print(a & b) #交集{1, 'a'}相同的
print(a-b)   #差集{2, 3, 'b'}a有b没有
print(a | b) #并集{1, 2, 3, 33, 'a', 22, 'b'}都有的并且去重
print(a^b)   #对称差集{33, 2, 3, 22, 'b'}把ab中重复的去掉





