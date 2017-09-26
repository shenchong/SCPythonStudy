# -*- coding: UTF-8 -*-

# SCModuleTest模块：
def moduleTest():
    print("我是moduleTest方法")
# 加了这个判断，则自己运行当前模块会执行，别的模块调用不会执行
if __name__ == "__main__":
    moduleTest()


# -*- coding: UTF-8 -*-

# SCModule模块：
import SCModuleTest
SCModuleTest.moduleTest()

# 另一种导入和调用方式
# import SCModuleTest as scm
# scm.moduleTest()