'''
计算字符串中子串出现的次数
'''
# ##method1:
# str='hello world'
# count=0
# for i in str:
#     if i=='o':
#         count+=1
# print('o在字符串中出现了%d次'%count)


##method2
if __name__ == '__main__':
    str1 = input('请输入一个字符串:\n')
    str2 =input('请输入一个子字符串:\n')
    count = str1.count(str2)
    print(count)
