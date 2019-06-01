'''
求0—7所能组成的奇数个数
'''

##method1:need a long time delete
#确定0-7能组成数的个数，再去掉个位为偶数的数

a=[]
for i in range(1,8):  #一位数
    a.append(i)
for i in range(1,8):   #两位数
    for j in range(8):
        if j!=i:
            a.append((10*i+j))
for i in range(1,8):  #三位数
    for j in range(8):
        for k in range(8):
            if i!=j and j!=k:
                a.append((100*i+10*j+k))
for i in range(1,8):   #四位数
    for j in range(8):
        for k in range(8):
            for l in range(8):
                if i!=j!=k!=l:
                    a.append(1000*i+100*j+10*k+l)
for i in range(1,8):   #五位数
    for j in range(8):
        for k in range(8):
            for l in range(8):
                for m in range(8):
                    if i!=j!=k!=l!=m:
                        a.append(10000*i+1000*j+100*k+10*l+m)

for i in range(1,8):   #六位数
    for j in range(8):
        for k in range(8):
            for l in range(8):
                for m in range(8):
                    for n in range(8):
                        if i!=j!=k!=l!=m!=n:
                            a.append(100000*i+10000*j+1000*k+100*l+10*m+n)
for i in range(1,8):   #七位数
    for j in range(8):
        for k in range(8):
            for l in range(8):
                for m in range(8):
                    for n in range(8):
                        for o in range(8):
                            if i!=j!=k!=l!=m!=n!=o:
                                a.append(1000000*i+100000*j+10000*k+1000*l+100*m+10*n+o)
for i in range(1,8):   #八位数
    for j in range(8):
        for k in range(8):
            for l in range(8):
                for m in range(8):
                    for n in range(8):
                        for o in range(8):
                            for p in range(8):
                                if i!=j!=k!=l!=m!=n!=o!=p:
                                    a.append(10000000*i+1000000*j+100000*k+10000*l+1000*m+100*n+10*o+p)
for i in a:
    if i%2==0:
        a.remove(i)
print(len(a))

# ##method2:
# '''
# 组成1位数是4个。
#
# 组成2位数是7*4个。
#
# 组成3位数是7*8*4个。
#
# 组成4位数是7*8*8*4个。
#
# ......
# '''
# if __name__ == '__main__':
#     sum = 4
#     s = 4
#     for j in range(2,9):
#         print(sum)
#         if j <= 2:
#             s *= 7
#         else:
#             s *= 8
#         sum += s
#     print('sum = %d' % sum)