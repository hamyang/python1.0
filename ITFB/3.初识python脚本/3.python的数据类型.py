#什么是数据类型
#数据类型就是数据的表现形式，比如 你好 就是一个字符串，200 就是一个数字等


#常用的数据类型
#1.字符串类型
love = 'iloveyou'
hello = '你好世界'
like = "i like you"
print(love,hello,like)
print(love)
print(hello)
print(like)
#在python提供了一个方法用于获取当前变量的数据类型，type()
#type函数 ， 返回一个数据或变量的数据类型
res = type(love)
print(res)
print(love,res)

#大字符串
s = '''
这是一个很长的文章
可以换行
'''
res = type(s)
print(s,res)

#可以嵌套别的引号'.'  "."  '''.'''
#单双引号可以相互嵌套，但是不能嵌套自己
s = 'i "love"you'
print(s)


#关于转义字符\n表示换行，\t表示制表符，r可以取消转义字符效果
s = '床前\n明月光'
print(s)
s = r'床前\n明月光'  #r可以取消转义字符效果
print(s)






