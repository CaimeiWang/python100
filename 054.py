#encoding:utf-8
##取一个整数a从右端开始的4〜7位
##method1:
# a=int(input('please input a number:'))
# b1=a%10000
# si=b1//1000
# b2=a%100000
# wu=b2//10000
# b3=a%1000000
# liu=b3//100000
# b4=a%10000000
# qi=b4//1000000
#print(si,wu,liu,qi)

##method2:(原来是按位计算啊)
'''
(1)先使a右移4位。 
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4) 
(3)将上面二者进行&运算。
'''
if __name__ == '__main__':
    a = int(input('input a number:'))  #a=10    1010
    b = a >> 4   #将a向右移4个单位  b=0000
    c = ~(1 << 4)    #10000取反    c=01111
    d = b & c    #d=0000=0
    print('%o\t%o' %(a,d))
##不懂a为啥变为了11