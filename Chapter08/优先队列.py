"""
author: Lns-XueFeng
CreateTime: 2023.04.09
"""


"""优先队列：
队列的一种变体：优先级队列 -> 比如操作系统中的多级优先队列

利用二叉堆Binary Heap实现优先级队列

注：在Python标准库中实现了一个堆队列算法
"""


class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, size):
        while size // 2 > 0:
            if self.heap_list[size] < self.heap_list[size//2]:
                temp = self.heap_list[size//2]
                self.heap_list[size // 2] = self.heap_list[size]
                self.heap_list[size] = temp
            size = size // 2

    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.perc_up(self.current_size)   # 上浮

    def min_child(self, index):
        if (index * 2 + 1) > self.current_size:
            return index * 2

        if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
            return index * 2

        return index * 2 + 1

    def perc_down(self, index):
        while (index * 2) <= self.current_size:
            mc = self.min_child(index)
            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[mc]
                self.heap_list[mc] = temp
            index = mc

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, a_list):
        index = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        print(len(self.heap_list), index)
        while index > 0:
            print(self.heap_list, index)
            self.perc_down(index)
            index -= 1
        print(self.heap_list, index)
