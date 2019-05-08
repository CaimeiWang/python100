#encoding:utf-8
##统计 1 到 100 之和
##method1:
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)


##method2:
a=[]
for i in range(1,101):
    a.append(i)
print(sum(a))