#encoding:utf-8
##两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

##method1
# jia=[['a'],['b'],['c']]
# yi=['x','y','z']
# for i in range(len(yi)-1):
#     if yi[i]!='x' and yi[i]!='z':
#         jia[2].append(yi[i])
#         yi.remove(yi[i])
#     if yi[i]!='x':
#          jia[0].append(yi[i])
#          yi.remove(yi[i])
#          jia[1].append(yi[0])
# print(jia)


##method2
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))
