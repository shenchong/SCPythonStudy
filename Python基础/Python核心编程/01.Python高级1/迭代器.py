# -*- coding: UTF-8 -*-

from collections import Iterable
from collections import Iterator

# 判断一个对象是否可以迭代,True为可以迭代：
print(isinstance("abc", Iterable))

# 判断是否为迭代器
print(isinstance((x for x in range(10)), Iterator))

# 用生成器创建迭代器
print(isinstance(iter("abc"), Iterator))