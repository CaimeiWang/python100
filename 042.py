#encoding:utf-8
##学习使用auto定义变量的用法
##method1


##method2
num=2
def autofun():
    num=1
    print('the internal num is %d:'%num)
    num=+1
for i in range(3):
    print('the num is %d:'%num)
    num+1
    autofun()