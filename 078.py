#找到年龄最大的人，并输出。

# #method1:
# age=[]
# person={'wang':25,'zhou':30,'zhao':28}
# val=person.values()
# for i in val:
#     age.append(i)
# print(max(age))



# ##method2:
# if __name__ == '__main__':
#     person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
#     m = 'li'
#     for key in person.keys():
#         if person[m] < person[key]:
#             m = key
#
#     print('%s,%d' % (m, person[m]))


##method3:
person={'wang':25,'zhou':30,'zhao':28}
inf=person.items()
age=[]
for value in person.values():
    age.append(value)
for key,value in inf:
    if value==max(age):
        print(key,value)