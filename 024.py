#encoding:utf-8
##有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和
##method1:analysis:分子分母都是斐波那契数列
# from fractions import Fraction
# a=[2,3] #放分子
# b=[1,2] #放分母
# for i in range(2,20):
#     a.append((a[i-2]+a[i-1]))
#     b.append((b[i-2]+b[i-1]))
# c=[]
# s=Fraction(0)
# for i in range(20):
#     s+=Fraction(a[i],b[i])
# print(s) #s输出结果为分数形式
# print(s.numerator/s.denominator)  #输出结果为小数形式

##method2:
# a = 2.0
# b = 1.0
# s = 0
# for n in range(1,21):
#     s += a / b
#     t = a
#     a = a + b
#     b = t
# print(s)  #输出结果为小数形式

##method3:
# a = 2.0
# b = 1.0
# s = 0.0
# for n in range(1, 21):
#     s += a / b
#     b, a = a, a + b
# print(s)

##method4:
from functools import reduce
a = 2.0
b = 1.0
l = []
l.append(a / b)
for n in range(1,20):
    b,a = a,a + b
    l.append(a / b)
print(reduce(lambda x,y: x + y,l))
