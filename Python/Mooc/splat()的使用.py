s= 'www.dod.com.cn'
# 默认分隔符
print(s.split())
#  . 分割
print(s.split('.'))
#  分割一次   2次
print(s.split('.',1))
print(s.split('.',2))
# 取出被 . 分割的下标为1的字符串
print(s.split('.',2)[1])
# 分割最多次实际与不加参数一样（默认分割富一样）
print(s.split('.',-1))
#分割三次并将分割的字符串保存到三个文件内
s1,s2,s3= s.split('.',2)
print(s1)
print(s3)
print(s2)

# 去掉换行符  \n  \t
c = '''hello
    world'''
print(c)
print(c.split('\n'))
print(c.split('\t'))

# 分离文件名和路径
#os.path.split()：按照路径将文件名和路径分割开
import  os
print(os.path.split('/dodo/soft/python/'))
print(os.path.split('/dodo/soft/python'))

#超级实例列举

a= 'hello boy<[www.dodo.com.cn]>byebye'
# 已[分割
print(a.split('['))
# 以【分割后取值下标为1的值，然后再次已】分割取下标为0的值
print(a.split('[')[1].split(']')[0])
# 以【分割后取值下标为1的值，然后再次以】分割取下标为0的值在次以。分割
print(a.split('[')[1].split(']')[0].split('.'))
