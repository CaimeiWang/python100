#encoding:utf-8
#输出 9*9 乘法口诀表
#9行9列，第i行有i列
##method1:
# a = []
# for i in range(1,10):#9lines
#     a.append([])
#     for j in range(1,i+1):
#       a[i-1].append(i*j)
# for i in range(1,10):
#     print('')
#     for j in range(1,i+1):
#         print(i, '*', j, '=', a[i - 1][j - 1],end='  ')



##method2:
for i in range(1, 10):
    print('')
    for j in range(1, i+1):
        print( "%d*%d=%d" % (i, j, i*j),end='  ')