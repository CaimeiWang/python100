#encoding:utf-8
# 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#
##method1:analysis:共有七行七列，可分为上下两部分
# a=[]
# for i in range(7):
#     a.append([])
# for i in range(4):
#     for j in range((4-i)):
#         a[i].append('')
#     for k in range((2*i+1)):
#         a[i].append('*')
# for j in range(4,7):
#     a[j]=a[6-j]
# for i in a:
#     print()
#     for j in i:
#        print(j,end=' ')

##method2:
from sys import stdout

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print()

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print()