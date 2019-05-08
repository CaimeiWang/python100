#encoding:utf-8
#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

##METHOD1:
# str=input('please input the string:')
# letters=0
# space=0
# digit=0
# others=0
# for i in str:
#      if i.isalpha():
#          letters+=1
#      elif i.isspace():
#          space+=1
#      elif i.isdigit():
#          digit+=1
#      else:
#          others+=1
# print('letters={} space={} digit={} others={}'.format(letters,space,digit,others))

##METHOD2:
str=input('please input the string:')
s=[]
for i in str:
    s.append(i)
letters=0
space=0
digit=0
others=0
i=0
while i<=len(str)-1:
    c=s[i]
    i+=1
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print('letters={},space={},digit={},others={}'.format(letters,space,digit,others))
