'''
字符串日期转换为易读的日期格式
'''

from dateutil import parser
print(parser.parse("Aug 28 2015 12:00AM"))
print(parser.parse('2019'))
print(parser.parse('201906111309'))