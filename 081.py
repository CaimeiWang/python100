'''
809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果
'''

# ##method1:
# for i in range(10,100):
#     if 809*i==800*i+9*i:
#         if len(str(809*i))==4 and len(str(8*i))==2 and len(str(9*i))==3:
#             print(i,809*i)


##method2:
a = 809
for i in range(10,100):
    b = i * a
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print(b,' = 800 * ', i, ' + 9 * ', i)