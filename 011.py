#encoding:utf-8
#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
#method1:将兔子分成可以生产的兔子，一个月大兔子和二个月大兔子
import numpy as np

def num(n):
    a = np.zeros(12)
    b = np.zeros(12)
    c = np.zeros(12)
    sum = [1]
    a[0] = 0
    b[0] = 1
    c[0] = 0
    for i in range(2,n+1):
        a[i-1]=a[i-2]+c[i-2]
        b[i-1]=a[i-1]
        c[i-1]=b[i-2]
        num=a[i-1]+b[i-1]+c[i-1]
        sum.append(num)
    if n==1:
        return sum[0]
    else:
        return sum[n-1]
print(num(3))
'''
#method 2:兔子的个数构成了一个斐波那契数列：
num=[1,1]
for i in range(3,13):
    num.append((num[i-3]+num[i-2]))
n=int(input('the month:'))
print(num[n-1])
