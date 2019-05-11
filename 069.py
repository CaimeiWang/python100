'''
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''
# #method1:
#
# def delete(a,id):
#     #id = 0
#     count = 0
#     for i in a:
#         if i!=0:
#             id+=1
#             count+=1
#         if id==3:
#             a[i-1]=0
#             id=0
#     #print(a,count,id)
#     if count>3:
#         delete(a,id)
#     return a
# if __name__=='__main__':
#     n=int(input('please input the number of the people:'))
#     a = []
#     for i in range(n):
#         a.append(i + 1)
#     a=delete(a,0)
#     for i in a:
#         if i!=0:
#             print(a.index(i))




#method2:
if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0: k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n: i = 0

    i = 0
    while num[i] == 0: i += 1
    print(num[i])