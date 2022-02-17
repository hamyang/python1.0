
# while 循环
num = 1
while num <= 10:
    print(num)
    num += 1


# for 循环 通常for循环用来遍历一个容器类型的数据

vars = 'abcdefg'
# vars = [1,2,3,4]
# 使用for in 循环遍历容器数据类型 i相当于容器中的每一个元素
for i in vars:
    print(i)

for i in range(0,10):  #函数range（可迭对象）0开始10之前的9结束
    print(i)


'''
1.break 语句 结束 跳出
2.continue 语句 跳过
3.pass 语句 占位

range() 是一个函数，返回一个迭代对象

'''
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue #跳过本次循环
    else:
        print(num)

    if num == 7:
      break #跳出循环，后面不在执行，本次循环结束
#      quit()
    print('abc')


# 1.exit()
# 2.quit()
# 是用于结束当前python解释器程序，而break 和 continue是用来控制程序的