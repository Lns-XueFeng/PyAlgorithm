"""
author: Lns-XueFeng
CreateTime: 2023.03.23
"""

"""
快速排序使用分而治之来获得与归并排序相同的优点, 而不使用额外的存储, 
然而, 作为权衡, 有可能列表不能被分成两半, 当这种情况发生时, 我们将看到性能降低, 

快速排序首先选择一个值, 该值称为 枢轴值, 
虽然有很多不同的方法来选择枢轴值, 我们将使用列表中的第一项, 
枢轴值的作用是帮助拆分列表, 枢轴值属于最终排序列表（通常称为拆分点）的实际位置, 
将用于将列表划分为快速排序的后续调用, 
"""


def quick_sort(a_list):
    quick_short_helper(a_list, 0, len(a_list) - 1)


def quick_short_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_short_helper(a_list, first, split_point - 1)
        quick_short_helper(a_list, split_point + 1, last)


def partition(a_list, first, last):
    pivot_value = a_list[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp

    return right_mark


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(li)
print(li)
