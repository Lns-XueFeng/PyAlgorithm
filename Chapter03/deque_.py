"""
author: Lns-XueFeng
CreateTime: 2023.03.07
"""


# 双端队列：一种有序结构，数据的入队和出队可以在两端都发生，队首既可以入队也可以出队，队尾亦是
# 特征是两端都可以入队和出队
# 回文字判定这种问题就很适合用双端队列来解决，例如”ABCDCBA“、”上海自来水来自海上“等是回文字


class Deque:
    def __init__(self):
        self.__items = []   # 定义列表左端为队尾，右端为队首

    def add_front(self, item):
        """从队首添加一个元素"""
        self.__items.append(item)

    def remove_front(self):
        """从队首移除一个元素"""
        return self.__items.pop()

    def add_rear(self, item):
        """从队尾添加一个元素"""
        self.__items.insert(0, item)

    def remove_rear(self):
        """从队尾移除一个元素"""
        return self.__items.pop(0)

    def is_empty(self):
        return len(self.__items) == 0

    def items(self):
        return self.__items

    def length(self):
        return len(self.__items)
