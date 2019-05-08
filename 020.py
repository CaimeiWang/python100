#encoding:utf-8
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
##meyhod1:
# h=100  #初始高度
# a=[50] #第一次反跳距离(a[]存在每次反跳距离)
# l=0
# while a[l]>0:
#     a.append(a[l]/2)
#     l+=1
# print('第10次反跳高度：',a[9])  #第10次反跳高度
# b=[]
# for i in range(9):
#     b.append(a[i])
# h=h+2*sum(b)
# print('第10次落地共经过{}米'.format(h))

##method2:
tour = []
height = []

hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)

print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))