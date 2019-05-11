'''
写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
'''
# #method1
#
# def lenth(s):
#     print(len(s))
#
#
# if __name__=='__main__':
#     s=input('please input the char:')
#     lenth(s)


#method2:
if __name__ == '__main__':
    s = input('please input a string:\n')
    print('the string has %d characters.' % len(s))