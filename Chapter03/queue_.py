"""
author: Lns-XueFeng
CreateTime: 2023.03.05
"""


# 队列：一种有序结构，数据的入队与出队发生在不同端，入队一端称为队尾，出队一端则为队首
# 特征是后入后出，先入先出（FIFO），具有顺序特性，所存储的数据是需要一定次序的
# 判断一个问题是否适合用队列来解决，看其是否具有“排队等待”以及“入队出队”这两个特性


class Queue:
    def __init__(self):
        self.__items = []   # 定义列表左端为队尾，右端为队首

    def enqueue(self, item):
        self.__items.insert(0, item)

    def dequeue(self):
        return self.__items.pop()

    def isEmpty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def items(self):
        return self.__items
