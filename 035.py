#encoding:utf-8
##文本颜色设置

##method1:


##method2:
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(colors.WARNING + "警告的颜色字体?" + colors.BOLD)