#encoding:utf-8
#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+222
# 2+22222(此时共有5个数相加)，几个数相加由键盘控制

##method1:
digit=int(input('please input a digit:'))
num=int(input('please input the number:'))
i=0
a=[]
b=[]
while i<num:
    a.append(digit*10**i)
    i+=1
    b.append(sum(a))
#print(b)
print('{}='.format(sum(b)),end='')
for j in range(len(b)-1):
    print('{}+'.format(b[j]),end='')
print(b[-1])


##method2:
from functools import *
Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

#Sn = reduce(lambda x, y: x + y, Sn)
Sn=sum(Sn)
print("计算和为：", Sn)
