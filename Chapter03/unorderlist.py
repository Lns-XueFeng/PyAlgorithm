"""
author: Lns-XueFeng
CreateTime: 2023.03.07
"""


# 无序表：类似于Python所提供的列表，但实现的方法略有不同
# 利用链表实现无序表
# 怎样用链表实现无序表要熟练掌握


"""思路
Python列表之中的元素是相对安放的，因此我们要考虑这个特性
使用链表，就行一条链子一样把它们串起来，标识好开始端和结束端

链子上连接的元素，就称之为节点Node(value, nextNode)
Node3(10, node2) -- Node2(12, node3) --- Node1(6, None)
而UnOrderList中只需引用第一个Node1节点，其他均可通过相对引用找到
"""


class NotFoundValue(ValueError):
    pass


class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node

    def value(self):
        return self.__value


class UnOrderList:
    def __init__(self, *args):
        self.node = Node(list(args)[0])
        self.node.set_next(None)
        if len(args) > 1:
            for v in list(args)[1:]:
                new_node = Node(v)
                new_node.set_next(self.node)
                self.node = new_node

    def append(self, value):
        """将value添加到链表头部，但是是列表最右边"""
        new_node = Node(value)
        new_node.set_next(self.node)
        self.node = new_node

    def pop(self):
        """解绑链表头部的引用，新引用它的第二个"""
        self.node = self.node.get_next()

    def remove(self, value):
        """移除某个值，需处理两种情况"""
        current_node = self.node
        next_node = self.node.get_next()
        if current_node.value() == value:
            self.node = self.node.get_next()
            return

        while next_node is not None:
            if next_node.value() == value:
                current_node.set_next(next_node.get_next())
                return
            current_node = next_node
            next_node = current_node.get_next()
        raise NotFoundValue

    def length(self):
        """遍历计算无序表的长度，并且为insert的实现提供便利"""
        current_node = self.node
        count = 1
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
            count += 1
        return count

    def insert(self, index, value):
        """
        因为我们的无序表索引与Python List保持一致
        所以传入的index需要被length减去（注意索引从0开始）
        得到需要插入的正确位置
        """
        un_order_list_length = self.length()
        assert index < un_order_list_length

        pin = un_order_list_length - index
        count = 1
        current_node = self.node
        while current_node.get_next() is not None:
            if count == pin:
                new_node = Node(value)
                new_node.set_next(current_node.get_next())
                current_node.set_next(new_node)
                return
            count += 1
            current_node = current_node.get_next()

        if current_node.get_next() is None:
            new_node = Node(value)
            new_node.set_next(None)
            current_node.set_next(new_node)

    def index(self, value):
        """从后往前遍历，因此最后需要用无序表长度-count"""
        count = 1
        un_order_list_length = self.length()
        current_node = self.node

        while current_node.get_next() is not None:
            if current_node.value() == value:
                return un_order_list_length - count
            count += 1
            current_node = current_node.get_next()

        if current_node.get_next() is None:
            if current_node.value() == value:
                return un_order_list_length - count
        raise NotFoundValue

    def reverse(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


if __name__ == "__main__":
    # 提供两种创建方式，根据这个方式来编写具体代码
    list_ex_ = UnOrderList(2)
    list_ = UnOrderList(1, 2, 3)

    # 手动遍历：验证实现的正确性
    print(list_.node.value())
    n_node = list_.node.get_next()
    print(n_node.value())
    n_node = n_node.get_next()
    print(n_node.value())
    if n_node.get_next() is None:
        print("到达链表尾部")

    # 设计功能调用方法
    list_.append(4)
    list_.pop()
    list_.remove(3)
    list_.insert(0, 'a')   # a, 1, 2
    print(list_.index('a'))
    list_.reverse()
