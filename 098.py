'''
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
'''
# ##method1:
# lower=input('please input a lower-case letter')
# captical=lower.upper()
# with open('test','a') as f:
#     f.write(captical)
# f.close()

##method2:
if __name__ == '__main__':
    fp = open('test1.txt','w')
    string = input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test1.txt','r')
    print(fp.read())
    fp.close()