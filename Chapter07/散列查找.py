"""
author: Lns-XueFeng
CreateTime: 2023.03.28
"""

"""散列查找
通过散列实现高效的查找方案, 
准备一个线性表, 一开始均设置为None,
当需要往里面放值时, 通过散列函数计算应该放在那个位置, 
当需要从里面取值时, 通过散列函数计算其在那个位置或是否存在, 
此即实现了一个个元素对对应位置的映射, 但是如果位置不够多, 
且散列函数不够完美, 就会造成多个值会映射到一个位置, 
因此增加位置以及改善散列函数是首要问题, 解决方法有以下：
1.增加位置的数量, 但是过于浪费, 如果事先准备了一千个位置, 最终只用了几十个...
2.线性探测, 再散列, 会造成聚集效应
3.链表法：我要选用的方法, 如果发生散列冲突, 那就将这个值链接到当前位置的节点, 看起来就像有了一个个桶一样

最著名的近似完美的散列函数：MD5和SHA
完美散列函数可用于对文件一致性的校验, 仅对比其散列值即可知道其是否一致
亦可用于加密密码, 这样即可只保存用户密码的散列值, 仅对比散列值判断是否输入正确
最酷的应用-:>区块链技术
"""


class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_):
        self.__next = next_

    def get_value(self):
        return self.__value


class HashTable:
    """思路
    设置两个列表, __keys与__values, 初始值均为None
    我选用的是当遇到hash_函数计算的值是一样的时用链表法, 进行链接, 那么就需要Node ADT
    __setitem__实现了设置key和value, 当遇到要到同一个槽的时, 新节点链接旧节点, 新节点替换旧节点所在位置
    想象这两个列表每一个位置都有一个竖直的桶, 新加入的节点总是在最上方
    __getitem__实现了取key和value, 先取判断key的hash_值是否再相应位置有Node,
    如果有那么就去查看当前节点是否就是key, 如果是那么就返回value, 如果不是, 就去循环遍历链表去找对应的key, 同时用count记录找了几次
    如果找到了, 那么利用count的次数去循环到对应的__values的链表中对应的位置的值, 然后返回

    按照__setitem__实现的算法大概是这种样子, 最重要的是就算是两个key算出来的hash_值一样, 照样可以找到对应的value
    [-, -, -, -, -, -, -, -]   [-, -, -, -, -, -, -, -]
     |  |  |     |  |  |  |     |  |  |     |  |  |  |
     |     |        |     |     |     |        |     |
     |                          |
    """
    def __init__(self):
        self.size = 11
        self.__keys = [None] * self.size
        self.__values = [None] * self.size

    def hash_(self, key: int or str) -> int:
        if isinstance(key, str):
            st = list(key)
            count = 1
            total = 0
            for s in st:
                a_num = ord(s) * count
                total = total + a_num
                count = count + 1
            return total % self.size
        return key % self.size

    def __getitem__(self, key):
        index = self.hash_(key)
        temp_k = self.__keys[index]
        temp_v = self.__values[index]
        if temp_k is None:
            return None
        elif isinstance(temp_k, Node) and isinstance(temp_v, Node):
            # 如果第一个就是key, 那么返回value
            if temp_k.get_value() == key:
                return temp_v.get_value()
        else:
            raise TypeError
        count = 0   # 计算循环了几次找到key, 然后用来找value
        # 寻找对应的keyNode
        while temp_k.get_value() != key:
            # 如果都到最底下了都还没找到, 说明没这个key的value
            if temp_k.get_next() is None:
                return None
            temp_k = temp_k.get_next()
            count = count + 1
        # 寻找对应的valueNode
        while count != 0:
            temp_v = temp_v.get_next()
            count = count - 1
        return temp_v.get_value()

    def __setitem__(self, key, value):
        index = self.hash_(key)
        if self.__keys[index] is None:
            self.__keys[index] = Node(key)
        else:
            new_node = Node(key)
            new_node.set_next(self.__keys[index])
            self.__keys[index] = new_node

        if self.__values[index] is None:
            self.__values[index] = Node(value)
        else:
            new_node = Node(value)
            new_node.set_next(self.__values[index])
            self.__values[index] = new_node


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    H["cat"] = 54
    H["dog"] = 26
    H["lion"] = 93
    H["tiger"] = 17
    H["bird"] = 77
    H["cow"] = 31
    H["goat"] = 44
    H["pig"] = 55
    H["chicken"] = 20
    print("-----------")
    for s in [54, 26, 93, 17, 77, 31, 44, 55, 20,
              "cat", "dog", "lion", "tiger", "bird", "cow", "goat", "pig", "chicken"]:
        print(H[s])
    print("-----------")
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9,
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
        print(H[n])
    print("-----------")
