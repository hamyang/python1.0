
# 十进制 转为 二进制
#bin()可以转为二进制
#int()可以转为十进制
a = 125
print(bin(a))

a = 0b1111101
print(int(a))

#左移动运算符 <<
'''
 运算数的各二进制位全部左移若干位 高位丢弃地位补0

'''
a = 0b00111100   #对于十进制为125
print(int(a<<2)) #11110000结果为240

#右移动运算符 >>












