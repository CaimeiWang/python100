#encoding:utf-8
'''
输入3个数a,b,c，按大小顺序输出
'''
#method1:
# num=[]
# a=int(input('please input the first number:'))
# num.append(a)
# b=int(input('please input the second number:'))
# num.append(b)
# c=int(input("please input the third number:"))
# num.append(c)
# #print(num)
# print(sorted(num))
# print(sorted(num,reverse=True))


#method2:
if __name__ == '__main__':
    n1 = int(input('n1 = :\n'))
    n2 = int(input('n2 = :\n'))
    n3 = int(input('n3 = :\n'))


    def swap(p1, p2):
        return p2, p1


    if n1 > n2: n1, n2 = swap(n1, n2)
    #print(n1,n2)
    if n1 > n3: n1, n3 = swap(n1, n3)
    #print(n1,n3)
    if n2 > n3: n2, n3 = swap(n2, n3)
    #print(n2,n3)

    print(n1, n2, n3)