# -*- coding: UTF-8 -*-

import sys
# sys.argv接收程序的参数
print(sys.argv)
name = sys.argv[1]
print("我是%s"%(name))

# 终端运行的时候，Python 给程序传参.py {name}