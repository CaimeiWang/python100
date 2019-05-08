#encoding：utf-8
##企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# i=int(input('please input the profit:'))
# b1=10*0.1
# b2=b1+10*0.075
# b3=b2+20*0.05
# b4=b3+20*0.03
# b5=b4+40*0.015
# if i<10 or i==10:
#     bonus=0.1*i
# elif i>10 and i<=20:
#     bonus=b1+(i-10)*0.075
# elif i>20 and i<=40:
#     bonus=b2+(i-20)*0.05
# elif i>40 and i<=60:
#     bonus=b3+(i-40)*0.03
# elif i>60 and  i<=100:
#     bonus=b4+(i-60)*0.015
# elif i>100:
#     bonus=b5+(i-100)*0.001
# print(bonus)


##method2:
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)
