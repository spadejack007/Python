#!/usr/bin/env python
#encoding: utf-8
#注意：从网页上复制时，有些空格字符不一致；实际运行时会报错，需要全部修改或替换为空格
import turtle
import math

turtle.delay(1)
t=turtle.Pen()
 
#setPen()画笔定位子程序模块是画圆和画五角星模块都要调用到的
def setPen(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
 
#drawCircle()画圆子程序模块
def drawCircle(x,y,r,color):
    t.pencolor(color)
    t.fillcolor(color)
    setPen(x,y-r)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
 
#画五角星子程序模块
def drawFiveStars(r):
    setPen(0,r) #A点坐标为画五角星的起点坐标
    t.right(72) #向右转过72度
    t.pencolor('whitesmoke')
    t.fillcolor("whitesmoke")
    t.begin_fill()
    for i in range(5):
        #线长a =r*2*cos(18°) =120*2*cos(18°) =240*0.951 =228
        #18*math.pi/180 为了将角度转换为弧度
        t.forward(r*2*math.cos(18*math.pi/180))#这个地方还是没有太明白
        t.right(144)
    t.end_fill()
 
#drawShield()画盾牌子程序模块
def drawShield():
    drawCircle(0,0,240,'red')#四个以O（0，0）圆心的同心圆
    drawCircle(0,0,200,'white')
    drawCircle(0,0,160,'red')
    drawCircle(0,0,120,'blue')#最里面的小圆半径为120
    drawFiveStars(120)#五角星的内接圆半径为120
 
#采用“模块化”设计方案。if __name__=='__main__' 为主程序入口
if __name__=='__main__':
    drawShield()
    turtle.done()
