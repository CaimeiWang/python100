#编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

# ##method1：
# def add(n):
#     if n%2==0:
#         res=0
#         for i in range(2,n+1,2):
#             res+=1/i
#         print('1/2+...+1/{}={}'.format(n,res))
#     else:
#         res=0
#         for i in range(1,n+1,2):
#             res+=1/i
#         print('1/1+...+1/{}={}'.format(n,res))
# if __name__=="__main__":
#     n=int(input('please input n:'))
#     add(n)

##method2:
def peven(n):
    i = 0
    s = 0.0
    for i in range(2, n + 1, 2):
        s += 1.0 / i  # Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
    return s


def podd(n):
    s = 0.0
    for i in range(1, n + 1, 2):
        s += 1.0 / i  # Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
    return s


def dcall(fp, n):
    s = fp(n)
    return s


if __name__ == '__main__':
    n = int(input('input a number:\n'))
    if n % 2 == 0:
        sum = dcall(peven, n)
    else:
        sum = dcall(podd, n)
    print(sum)