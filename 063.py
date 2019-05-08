#encoding:utf-8
'''
画椭圆
'''
# #method1
# from tkinter import *
# window=Tk()
# window.title('voval')
# canvas=Canvas(width=300,height=300,bg='blue')
# canvas.pack()
# x0=50
# y0=50
# x1=200
# y1=250
# canvas.create_oval(x0,y0,x1,y1,width=5,fill='yellow')
# mainloop()

#method2
if __name__ == '__main__':
    from tkinter import *

    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()