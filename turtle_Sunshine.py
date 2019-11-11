#!/usr/bin/env python
# encoding: utf-8

from turtle import *
color('red', 'yellow')#画笔为红色，里面为黄色

begin_fill()#begin_fill和end_fill所绘制的图形进行填充
while True:
    forward(200)#从(0,0)原点位置起，画200像素长度的线段
    left(170)#向左倾斜170度继续画图
    if abs(pos()) < 1:#abs计算位置，还需要深入查看；此处是退出条件
        break
end_fill()#begin_fill和end_fill所绘制的图形进行填充
done()