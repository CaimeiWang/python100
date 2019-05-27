#
if __name__ == '__main__':
    for i in range(5):   #(i=0,1,2,3,4)
        n = 0
        if i != 1: n += 1     #每一个都执行
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3: print(64 + i)