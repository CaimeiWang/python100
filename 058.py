#encoding:utf-8
'''
画图，学用rectangle画方形
'''

# #mwthod1
# from tkinter import *
# canvas=Canvas(width=300,height=300,bg='red')
# canvas.pack()
# x0=50
# y0=50
# x1=200
# y1=200
# canvas.create_rectangle(x0,y0,x1,y1,width=5,fill='yellow')
# mainloop()


#method2
if __name__ == '__main__':
    from tkinter import *

    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width=400, height=400, bg='yellow')
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()