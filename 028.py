#encoding:utf-8
##有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
# 问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
# 最后问第一个人，他说是10岁。请问第五个人多大？
##method1:
a=10
for i in range(2,6):
    a+=2
print('the age of the fifth person is:%d'%a)


##method2:
def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n - 1) + 2
    return c
print(age(5))
