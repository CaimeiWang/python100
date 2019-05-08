#encoding:utf-8
##利用递归方法求5!
##method1:
# a=1
# for i in range(1,6):
#     a*=i
# print('5!=%d'%a)  ##错：没有体现递归

##method2:
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum

print(fact(5))