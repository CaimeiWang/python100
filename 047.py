#encoding:utf-8
##两个变量值互换
##method1:
# def exchange():
#     a=input('please input the first number:')
#     b=input('please input the second number:')
#     c=a
#     a,b=b,c
#     print(a,b)
# exchange()

##method2:
def exchange(a, b):
    a, b = b, a
    return (a, b)


if __name__ == '__main__':
    x = 10
    y = 20
    print('x = %d,y = %d' % (x, y))
    x, y = exchange(x, y)
    print('x = %d,y = %d' % (x, y))