"""
author: Lns-XueFeng
CreateTime: 2023.03.23
"""

"""希尔排序
希尔排序(有时称为“递减递增排序”)通过将原始列表分解为多个较小的子列表来改进插入排序,
每个子列表使用插入排序进行排序, 选择这些子列表的方式是希尔排序的关键,
不是将列表拆分为连续项的子列表, 希尔排序使用增量i(有时称为 gap), 通过选择 i 个项的所有项来创建子列表
"""


def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:

        for start_position in range(sublist_count):
            gap_insert_sort(a_list, start_position, sublist_count)

        print("After increments of size", sublist_count, "The list is", a_list)

        sublist_count = sublist_count // 2


def gap_insert_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):

        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(li)
print(li)
