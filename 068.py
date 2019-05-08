<<<<<<< HEAD
#encoding:utf-8
'''
有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''

# #method1
# def move_digits(n,m):
#     num=[]
#     for i in range(n):
#         digit=input('please input the {} digit'.format(i+1))
#         num.append(digit)
#     for j in range(m):
#         num.insert(0,0)
#         num[0]=num[n]
#     del num[n:n+m]
#     for i in num:
#        print(i,end=' ')
#
# if __name__=="__main__":
#     move_digits(6,3)


##method2
if __name__ == '__main__':
    n = int(input('整数 n 为:\n'))
    m = int(input('向后移 m 个位置为:\n'))


    def move(array, n, m):
        array_end = array[n - 1]
        for i in range(n - 1, -1, - 1):
            array[i] = array[i - 1]
        array[0] = array_end
        m -= 1
        if m > 0: move(array, n, m)


    number = []
    for i in range(n):
        number.append(int(input('输入一个数字:\n')))
    print('原始列表:', number)

    move(number, n, m)

=======
#encoding:utf-8
'''
有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''

# #method1
# def move_digits(n,m):
#     num=[]
#     for i in range(n):
#         digit=input('please input the {} digit'.format(i+1))
#         num.append(digit)
#     for j in range(m):
#         num.insert(0,0)
#         num[0]=num[n]
#     del num[n:n+m]
#     for i in num:
#        print(i,end=' ')
#
# if __name__=="__main__":
#     move_digits(6,3)


##method2
if __name__ == '__main__':
    n = int(input('整数 n 为:\n'))
    m = int(input('向后移 m 个位置为:\n'))


    def move(array, n, m):
        array_end = array[n - 1]
        for i in range(n - 1, -1, - 1):
            array[i] = array[i - 1]
        array[0] = array_end
        m -= 1
        if m > 0: move(array, n, m)


    number = []
    for i in range(n):
        number.append(int(input('输入一个数字:\n')))
    print('原始列表:', number)

    move(number, n, m)

>>>>>>> a4f8e8d61598546e81645b5487af6f5cc64097ae
    print('移动之后:', number)