"""
author: Lns-XueFeng
CreateTime: 2023.03.23
"""

"""选择排序
选择排序改进了冒泡排序, 它也是扫描列表n次, 
但不是依次交换, 而是每一趟都找到最大的值, 然后与最右端值交换

标准定义：选择排序改进了冒泡排序, 
每次遍历列表只做一次交换, 为了做到这一点, 
一个选择排序在他遍历时寻找最大的值, 并在完成遍历后, 将其放置在正确的位置
"""


def select_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        position_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[position_max]:
                position_max = location

        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[position_max]
        a_list[position_max] = temp


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
select_sort(li)
print(li)
