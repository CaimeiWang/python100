#encoding:utf-8
#暂停一秒输出，并格式化当前时间
import time
# d={'1':'a','2':'b'}
# for key,value in dict.items(d):
#     print(key,value)
#     time.sleep(1) #停顿一秒
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.strftime( '%Y-%m-%d %A %H:%M:%S',time.localtime()))