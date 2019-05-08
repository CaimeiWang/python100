#encoding:utf-8
##按相反的顺序输出列表的值
##method1:
# def output(a,l):
#     if l==0:
#         return
#     else:
#         print(a[l-1],end=' ')
#     output(a,l-1)
# a=[1,2,3,4,5,6]
# l=len(a)
# output(a,l)

##method2:
# a=[1,2,3,4,5]
# l=len(a)
# while l>0:
#     print(a[-1],end=' ')
#     a.pop()
#     l=len(a)


##method3:
a = ['one', 'two', 'three']
for i in a[::-1]: ##步长为-1，输出列表中的元素
    print(i)