#encoding:utf-8
#斐波那契数列(输出100个数)
#method1:
# a=[0,1]
# for i in range(2,101):
#     m=a[i-1]+a[i-2]
#     a.append(m)
# for i in a:
#     print(i,end=' ')

# #method2:
# def fab(n):
#     if n==1 or n==2:
#         return 1
#     return (fab(n-1)+fab(n-2))
# print(fab(10))

##method3:
def fab(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,(a+b)
    return a
print(fab(10))