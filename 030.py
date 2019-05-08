#encoding:utf-8
##一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
##method1:
# num=int(input('please input a five-digit number:'))
# a=num//10000
# b=num%10000//1000
# c=num%1000//100
# d=num%100//10
# e=num%10
# if a==e and b==d:
#     print('%d是回文数'%num)
# else:
#     print('%d不是回文数'%num)


##method2:
a = int(input("请输入一个数字:\n"))
x = str(a)
flag = True

for i in range((len(x) // 2)):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print("%d 是一个回文数!" % a)
else:
    print("%d 不是一个回文数!" % a)