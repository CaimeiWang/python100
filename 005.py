#encoding:utf-8
##输入三个整数x,y,z，请把这三个数由小到大输出
##method1:
# a=[]
# x=int(input('please input the first number:'))
# a.append(x)
# y=int(input('please input the second number:'))
# a.append(y)
# z=int(input('please input the third number:'))
# a.append(z)
# a.sort()
# print(a)

##method2:
# x=int(input('please input the first number:'))
# y=int(input('please input the second number:'))
# z=int(input('please input the third number:'))
# if x>y:
#     x,y=y,x
#     if x>z:
#         x,z=z,x
#         if y>z:
#             y,z=z,y
#     elif y>z:
#         y,z=z,y
# elif x>z:
#     x,z=z,x
#     if y>z:
#         y,z=z,y
# elif y>z:
#     y,z=z,y
# print(x,y,z)

##method3:
l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)