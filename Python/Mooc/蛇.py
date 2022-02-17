import turtle
turtle.setup(650,350,200,200) #设置画框大小
turtle.penup()                #画笔抬起
turtle.fd(-250)               #长度像素-为倒退
turtle.pendown()              #画笔落下准备绘画
turtle.pensize(25)            #物体宽度
turtle.pencolor("purple")     #物体颜色
turtle.seth(0)                #起始方向
for i in range(4):            #循环

    turtle.circle(40,45)      #正向像素距离，40弧度
    #turtle.circle(-40,45)     #反向像素距离，45弧度
    turtle.circle(-30,35)     
turtle.circle(40,30)          #不太明白
turtle.fd(50)                 #直行像素长度
turtle.circle(-40,90)         #反向像素40距离，180弧度
turtle.fd(50)                 #直行长度
turtle.done()                 #防止运行完成后退出



