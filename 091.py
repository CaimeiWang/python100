'''
时间函数举例1
'''

if __name__ == '__main__':
    import time
    print(time.time())
    print(time.localtime())
    print(time.ctime())
    print(time.gmtime())
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))