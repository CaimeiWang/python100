#列表排序及连接。
if __name__=='__main__':
    a=[1,2,3,4]
    b=[5,6,7,8]
    #列表排序
    a.sort(reverse=True)
    print(a)
    #列表连接
    print(a+b)
    a.extend(b)
    print(a)