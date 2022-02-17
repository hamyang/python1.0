
# 流程控制




# 流程就是计算机执行的顺序，顺序结构，分支结构，循环结构

#双向分支：
person = '女'
if person == '女':
    #真区间
    print('向前搭讪')
else:
    #假区间
    print('向前借火')

#多向分支

score = int(input('输入考试成绩'))

if score < 60:
        print('给你个大嘴巴子')
elif score >= 90 and score <= 100:
        print('给你一个大大的奖励')
elif score >= 80 and score < 90:
        print('今晚吃顿好的，庆祝一下')
elif score >= 70 and score <= 80:
        print('下次继续努力')
elif score >= 60 and score <= 70:
        print('抓紧复习看下次')

#巢状分支：在分支条件中嵌套分支
'''
if 表达式a：
    if 表达式b：
        if表达式c:
            。。。。。
'''



#课后作业   输入年份判断生肖









