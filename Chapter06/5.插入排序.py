"""
author: Lns-XueFeng
CreateTime: 2023.03.23
"""

"""插入排序
它始终在列表的较低位置维护一个排序的子列表,
然后将每个新项 “插入” 回先前的子列表, 
使得排序的子列表称为较大的一个项
"""


def insert_sort(a_list):
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(li)
print(li)
