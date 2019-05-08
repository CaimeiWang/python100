#encoding:utf-8
##输入某年某月某日，判断这一天是这一年的第几天？
##method1:
#闰年：整百年/400,非整白年/4
# p=[0,31,28,31,30,31,30,31,31,30,31,30]
# r=[0,31,29,31,30,31,30,31,31,30,31,30]
# y=int(input('please input the year:'))
# m=int(input('please input the month:'))
# d=int(input('please input the day:'))
# sum=0
# if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0):
#     for i in range(m):
#         sum+=r[i]
#     print('这是这一年的第%d天'%(sum+d))
# else:
#     for i in range(m):
#         sum+=p[i]
#     print('这是这一年的第%d天' % (sum + d))

##method2:
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)