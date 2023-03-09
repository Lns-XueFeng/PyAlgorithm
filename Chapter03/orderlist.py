"""
author: Lns-XueFeng
CreateTime: 2023.03.07
"""


# 有序表：与无序表类似，但它的元素始终保持有序
# 利用链表实现有序表
# 怎样用链表实现有序表要熟练掌握


"""思路
有序表可以建立在无序表由链表实现的基础上进行实现
因为有序表与无序表的区别是它”始终保持有序“

因此在无序表的基础上，我们只需要保证”初始化时保持有序“和”添加元素时也有序“
"""


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


class OrderList:
    def __init__(self, *args: int):
        # 暂时用Python提供的内置函数实现参数的有序
        # 后续实现自己的sorted函数来实现初始化有序
        __order_list = sorted(list(args))

        self._node = Node(__order_list[0])
        self._node.set_next(None)
        if len(__order_list) > 1:
            for v in __order_list[1:]:
                new_node = Node(v)
                new_node.set_next(self._node)
                self._node = new_node

        self.__iter_next = None
        self.__next_run_one = False

    def add(self, value: int):
        """
        基于初始化已经排序的order_list
        add只需在插入的时候遍历链表，找到合适的地方插入即可
        """
        assert type(value) is int

        if value > self._node.value():
            new_node = Node(value)
            new_node.set_next(self._node)
            self._node = new_node
            return

        current_node = self._node
        while current_node.get_next() is not None:
            next_node = current_node.get_next()
            if current_node.value() > value > next_node.value():
                new_node = Node(value)
                new_node.set_next(next_node)
                current_node.set_next(new_node)
                return
            current_node = current_node.get_next()

        if value < current_node.value():
            new_node = Node(value)
            new_node.set_next(None)
            current_node.set_next(new_node)

    def remove(self, value):
        """同UnOrderList一致"""
        pass

    def pop(self):
        """同UnOrderList一致"""
        pass

    def length(self):
        """同UnOrderList一致"""
        pass

    def index(self, value):
        """同UnOrderList一致"""
        pass

    def reverse(self):
        """同UnOrderList一致"""
        pass

    def __iter__(self):
        """同UnOrderList一致"""
        pass

    def __next__(self):
        """同UnOrderList一致"""
        pass


if __name__ == "__main__":
    # 提供两种构建方式，不过在构建时就需保持其有序
    # 暂时仅支持int类型，如果想支持多种数据类型，可通过自定义魔法方法来实现多种类型的排序定义
    list_ex_ = OrderList(2)
    list_ = OrderList(10, 5, 1)   # 1, 2, 3 -> 头部最大，尾部最小

    # 手动遍历：验证实现的正确性
    print(list_._node.value())
    n_node = list_._node.get_next()
    print(n_node.value())
    n_node = n_node.get_next()
    print(n_node.value())
    if n_node.get_next() is None:
        print("到达链表尾部")

    list_ex_.add(3)
    list_ex_.add(0)
    # 手动遍历：验证实现的正确性
    print(list_ex_._node.value())
    n_node = list_ex_._node.get_next()
    print(n_node.value())
    n_node = n_node.get_next()
    print(n_node.value())
    if n_node.get_next() is None:
        print("到达链表尾部")
