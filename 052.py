#encoding:utf-8
##学习使用按位或 |
##method1:0|0=0  0|1=1  1|1=1
a=[2,3,4]  #2=010  #3=011 #4=100
for i in a:
    b=i|5   #5=101
    print(b)