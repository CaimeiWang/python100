#encoding:utf-8
##求1+2!+3!+...+20!的和
##method1:
# s=0
# for i in range(1,21):
#     c=1
#     for j in range(1,i+1):
#         c*=j
#     #print(c)
#     s+=c
# print('1!+2!+3!+...+20!=%d'%s)

##method2:
# n = 0
# s = 0
# t = 1
# for n in range(1,21):
#     t *= n
#     s += t
# print ('1! + 2! + 3! + ... + 20! = %d' % s)

##method3:
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
s = sum(map(op,l))
print ('1! + 2! + 3! + ... + 20! = %d' % s)