
# 注意 :在写代码时，一定要严格遵守python的语法要求

if True:
    pass # pass 在代码库中专门用于 占位
    print("你好")

#十二生肖 子鼠、丑牛、卯兔、寅虎、辰龙、巳蛇、午马、未羊、申猴、酉鸡、戌狗、亥猪
'''
year = int(input('请输入四位数年份:'))

if year % 12 == 0:
    print(f'{year}年是 ==> 申猴')
elif year % 12 ==1:
    print(f'{year}年是 ==> 酉鸡')
elif year % 12 == 2:
    print(f'{year}年是 ==> 戌狗')
elif year % 12 == 3:
    print(f'{year}年是 ==> 亥猪')
elif year % 12 == 4:
    print(f'{year}年是 ==> 丑牛')
elif year % 12 == 5:
    print(f'{year}年是 ==> 卯兔')
elif year % 12 == 6:
    print(f'{year}年是 ==> 寅虎')
elif year % 12 == 7:
    print(f'{year}年是 ==> 辰龙')
elif year % 12 == 8:
    print(f'{year}年是 ==> 巳蛇')
elif year % 12 == 9:
    print(f'{year}年是 ==> 午马')
else:
     print('输入年份错误')
'''

# 程序优化
year = int(input('请输入年份'))
varlist = ['子鼠', '丑牛','卯兔','寅虎','辰龙','巳蛇','午马','未羊','申猴','酉鸡','戌狗','亥猪']
print(varlist[year % 12])













