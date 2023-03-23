"""
author: Lns-XueFeng
CreateTime: 2023.03.23
"""


# 顺序查找(无序)
def search(li, value):
    for e in li:
        if e == value:
            return True
    return False


un_order_list = [2, 3, 4, 1, 9]
print(search(un_order_list, 9))


# 顺序查找(有序)
def search(li, value):
    for e in li:
        if e == value:
            return True
        if e > value:   # 有序可优化
            return False
    return False


order_list = [1, 3, 7, 10, 18, 21]   # 仅支持从小到大
print(search(order_list, 6))
