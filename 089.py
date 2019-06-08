'''
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
'''

# ##method1:
# s=''
# a=input('please input a data:')
# b=s.join(a)
# c=[]
# for i in b:
#      c.append((int(i)+5)%10)
# c[0],c[3]=c[3],c[0]
# c[1],c[2]=c[2],c[1]
# print('加密后的数字是：')
# for i in c:
#     print(i,end='')


##method2:
from sys import stdout

if __name__ == '__main__':
    a = int(input('输入四个数字:\n'))
    aa = []
    aa.append(a % 10)
    aa.append(a % 100 / 10)
    aa.append(a % 1000 / 100)
    aa.append(a / 1000)

    for i in range(4):
        aa[i] += 5
        aa[i] %= 10
    for i in range(2):
        aa[i], aa[3 - i] = aa[3 - i], aa[i]
    for i in range(3, -1, -1):
        stdout.write(str(aa[i]))