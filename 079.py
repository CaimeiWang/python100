#字符串排序

# #method1:
# str='hello python'
# list=[]
# for i in str:
#     list.append(i)
# list.sort()
# print(list)


##method 2:
if __name__ == '__main__':
    str1 = input('input string:\n')
    str2 = input('input string:\n')
    str3 = input('input string:\n')
    print(str1, str2, str3)

    if str1 > str2: str1, str2 = str2, str1
    if str1 > str3: str1, str3 = str3, str1
    if str2 > str3: str2, str3 = str3, str2

    print('after being sorted.')
    print(str1, str2, str3)