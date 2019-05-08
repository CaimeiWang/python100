#encoding:utf-8
##学习使用按位取反~  ~0=1; ~1=0;
##method1:


##method2:  ？？？？

if __name__ == '__main__':
    a = 234  #11101010
    b = ~a   #00010101
    print('The a\'s 1 complement is %d' % b)
    a = ~a
    print('The a\'s 2 complement is %d' % a)