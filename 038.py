#encoding:utf-8
##求一个3*3矩阵主对角线元素之和。
##method1
# a=[(1,2,3),(4,5,6),(7,8,9)]
# sum=a[0][0]+a[1][1]+a[2][2]
# print(sum)

##method2
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print(sum)