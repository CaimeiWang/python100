#encoding:utf-8
##将一个数组逆序输出
##nethod1:
# if __name__ == '__main__':
#     a=[1,2,3,4,5,6,7]
#     l = len(a)
#     def output(a,l):
#         for i in range(l+1):
#             if l>0:
#                 print(a[l-1])
#                 l-=1
#     output(a,l)

##method2:
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a)
    print(a)
    for i in range(len(a) // 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print(a)