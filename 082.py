'''
八进制转换为十进制
'''
# ##method1:
# octal_number=int(input('please input an octal number:'))
# #先把八进制在转化为十进制
# s=str(octal_number)
# decimal=0
# for i in range(1,len(s)+1):
#     decimal+=int(s[-i])*8**(i-1)
# print("the decimal number is：",decimal)
#
# #再把十进制转化为十六进制
# dexadecimal=[]
# if decimal//16==0:
#     print('the dexadecimal number is:',decimal)
# else:
#     while decimal//16!=0:
#         quotient=decimal//16
#         remainder=decimal%16
#         dexadecimal.append(remainder)
#         decimal=quotient
#         print('the dexadecimal number is:')
#     if decimal//16==0:
#         dexadecimal.append(decimal%16)
#         dexadecimal.reverse()
#     for i in dexadecimal:
#         print(i,end='')


##method2:
if __name__ == '__main__':
    n = 0
    p =input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0') #ord() 返回对应的十进制整数   ord(0)=48
    print(n)
