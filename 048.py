#encoding:utf-8
##数字比较
##method1:
# a=int(input('please input the first number:'))
# b=int(input('please input the second number:'))
# if a>b:
#     print('{}>{}'.format(a,b))
# elif a==b:
#     print('{}={}'.format(a,b))
# else:
#     print('{}<{}'.format(a,b))


##method2:
if __name__ == '__main__':
    i = 10
    j = 20
    if i > j:
        print('%d 大于 %d' % (i,j))
    elif i == j:
        print('%d 等于 %d' % (i,j))
    elif i < j:
        print('%d 小于 %d' % (i,j))
    else:
        print('未知')