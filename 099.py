'''
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中
'''
# ##method1:
# list=[]
# with open('a.txt','r') as f1:
#     aline=f1.read()
#     for a in aline:
#        list.append(a)
# with open('b.txt','r') as f2:
#     bline=f2.read()
#     for b in bline:
#        list.append(b)
# list=sorted(list)
# print(list)
# with open('c.txt','w') as f3:
#     for i in list:
#        f3.write(i)
# with open('c.txt','r') as f:
#     print(f.read())

##method2:
if __name__ == '__main__':
    import string

    fp = open('a.txt')
    a = fp.read()
    fp.close()

    fp = open('b.txt')
    b = fp.read()
    fp.close()

    fp = open('c.txt', 'w')
    l = list(a + b)
    l.sort()
    s = ''
    s = s.join(l)
    fp.write(s)
    fp.close()