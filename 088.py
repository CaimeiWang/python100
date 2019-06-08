'''
读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
'''

# ##method1:
# import random
# l=[]
# for i in range(7):
#   a=random.randint(1,51)
#   l.append(a)
# print(l)
#
# for i in l:
#   b = ''
#   for j in range(i):
#     b+='*'
#   print(b)


##method2:
if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(input('input a number:\n'))
        print(a * '*')
        n += 1