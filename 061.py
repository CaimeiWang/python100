#输出10行杨辉三角
'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
.....
第i行有i个元素
'''
##method1
# import numpy as np
# a=np.zeros([10,10])
# a[0][0]=1
# a[1][0]=1
# a[1][1]=1
# #print(a)
# for i in range(2,10):
#     for j in range(1,i):
#         a[i][0]=1
#         a[i][i]=1
#         a[i][j]=a[i-1][j-1]+a[i-1][j]
# for i in range(10):
#     print(end='\n')
#     for j in range(10):
#         if a[i][j]!=0:
#             print(int(a[i][j]),end='  ')




##method2
if __name__=="__main__":
    #构造一个10行10列的矩阵
    a=[]
    for i in range(10):
        a.append([]) #构造10列
        for j in range(10):
            a[i].append(0)  #构造10行
    for i in range(10):#第一位和最后一位都为1
        a[i][0]=1
        a[i][i]=1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j]=a[i-1][j-1]+a[i-1][j]

    from sys import stdout
    for i in range(10):
        for j in range(i+1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        stdout.write('\n')#按行输出
        print

