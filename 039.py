#encoding:utf-8
##有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
#method1:
# a=[1,3,7,15,16]
# b=[16,8,5,4,2,1]
# w=int(input('please input a number:'))
# b.append(w)
# if b[0]>b[1]:
#     b.sort(reverse=True)
# else:
#     b.sort(reverse=False)
# print(b)

##method2:
#首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
if __name__ == '__main__':
    # 方法一 ： 0 作为加入数字的占位符
    a = [1,4,6,9,13,16,19,28,40,100,0]
    print('原始列表:')
    for i in range(len(a)):
        print(a[i])
    number = int(input("\n插入一个数字:\n"))
    end = a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    print('排序后列表:')
    for i in range(11):
        print(a[i])