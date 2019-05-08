#encoding:utf-8
##求100之内的素数(素数就是质数)
##method1:
# a=[]
# print(1)
# for i in range(101):
#     a.append([])
#     for j in range(1,i+1):
#         if i%j==0:
#            a[i].append(j)
#     if len(a[i])==2:
#         print(a[i][1])

##method2:
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
