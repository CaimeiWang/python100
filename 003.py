#encoding:utf-8
##一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
##method1:
# from math import *
# for i in range(1000):
#     a=i+100
#     sa=int(sqrt(a))
#     b=a+168
#     sb=int(sqrt(b))
#     if sa**2==a and sb**2==b:
#         print(i)


##method2:
for i in range(1,85):
    if 168 % i == 0:
        j = 168 / i;
        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)