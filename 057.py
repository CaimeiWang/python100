#encoding:utf-8
##画图，学用line画直线
##menthod1:
'''
if __name__ == '__main__':

    from tkinter import *
    canvas = Canvas(width=300, height=300,bg='yellow')  #画布尺寸和背景颜色
    canvas.pack(expand=YES, fill=BOTH)  #使画布正常显示
    #canvas.pack()
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='green')
        x0 += 5
        y0 += 5
        y1 += 5
    mainloop()
'''
'''
##method2
from tkinter import *
canvas=Canvas(width=300,height=300,bg='yellow')
canvas.pack(expand=NO,fill=BOTH)
x1,y1=50,20
x2,y2=100,20
x3,y3=75,40
x4,y4=75,100
canvas.create_line(x1,y1,x3,y3, width=3, fill='red')
canvas.create_line(x2,y2,x3,y3, width=3, fill='green')
canvas.create_line(x1,y1,x4,y4, width=3, fill='blue')
canvas.create_line(x2,y2,x4,y4, width=3, fill='purple')
mainloop()
'''

##method3:
import turtle
def drawline(n):
    t=turtle.Pen()
    t.color(0.3,0.8,0.6)  #设置颜色，在0--1之间
    t.begin_fill()   #开始填充颜色
    for i in range(n): #任意边形
        t.forward(50)
        t.left(360/n)
    t.end_fill()    #结束填充颜色

drawline(4)