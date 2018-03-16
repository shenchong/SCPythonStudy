# -*- coding: UTF-8 -*-

# 捕获异常：
try:
    b = 11
    # a = 11/0
    # open("xxx.txt")
    # print(num)
except (NameError,IOError):
    print("捕获到NameError or IOError异常")
except Exception as ret:
    print("没有捕获到上面列出的异常")
    print(ret,"--Exception as ret--这样可以打印出异常的详情")
else:
    print("没有异常才会执行")
finally:
    print("不管有没有异常最后都会执行")

print("执行完上述代码再执行")


# 处理自定义的异常：
class TooShortYouSend(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

def main():
    try:
        str = raw_input("请输入一个字符串：")
        if len(str)<3:
            raise TooShortYouSend(len(str), 3)
    except TooShortYouSend as result:
        print("TooShortYouSend: 你输入的字符串长度是: %s, 最少输入的长度是: %s" % (result.length, result.atleast))
    else:
        print("没有异常")
main()

