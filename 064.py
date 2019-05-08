#encoding:utf-8
'''
利用ellipse 和 rectangle 画图
'''
#method1
from tkinter import *
window=Tk()
window.title('circle')
canvas=Canvas(width=500,height=500,bg='blue')
canvas.pack()
x0=0
y0=0
x1=50
y1=50
x2=200
y2=200
x3=300
y3=300
for i in range(10):
    canvas.create_rectangle(x0,y0,x1,y1+10,width=3,fill=None)
    x1=x1+10
    y1=y1+10
for j in range(5):
    canvas.create_oval(x2,y2,x3,y3)
    x2=x2-50
    y2=y2-20
    x3=x3+50
    y3=y3+20
mainloop()