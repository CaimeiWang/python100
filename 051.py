#encoding:utf-8
##学习使用按位与 &
##method1:


##method2:0&0=0; 0&1=0; 1&0=0; 1&1=1
if __name__ == '__main__':
    a = [0,7,7]   #0=000  7=111
    for i in a:
        b = i & 3   #3=011
        print('a & b = %d' % b)
        b &= 7
        print('a & b = %d' % b)