"""
author: Lns-XueFeng
CreateTime: 2023.03.23
"""

"""归并排序
我们现在将注意力转向使用分而治之策略作为提高排序算法性能的一种方法,
我们将研究的第一个算法是归并排序, 归并排序是一种递归算法，不断将列表拆分为一半,
如果列表为空或有一个项, 则按定义（基本情况）进行排序,
如果列表有多个项, 我们分割列表, 并递归调用两个半部分的合并排序,
一旦对这两半排序完成, 就执行称为合并的基本操作,
合并是获取两个较小的排序列表并将它们组合成单个排序的新列表的过程,
"""


def mergeSort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("Merging ", a_list)


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(li)
print(li)
