"""
author: Lns-XueFeng
CreateTime: 2023.03.01
"""

# 栈：一种有序结构，数据的存入与取出仅发生在一端，这端被称为栈顶，另一端为栈底
# 特征是先进后出，后进先出（LIFO）
# 判断一个问题是是否适合利用栈解决，看其是否有反转，单一进出以及先进后出等特性来选用此数据结构


class Stack:
    def __init__(self):
        self.__items = []   # 规定列表左边为栈底，右边为栈顶

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def isEmpty(self):
        return len(self.__items) == 0

    def items(self):
        return self.__items

    def see_top(self):
        return self.__items[-1]   # 为方便OJ题2的解决
