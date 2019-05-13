'''
反向输出一个链表
'''
# #method1:
# list=[]
# for i in range(5):
#     num=int(input('please input the num:'))
#     list.append(num)
# for i in range(1,6):
#     print(list[-i])


#method2:
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)