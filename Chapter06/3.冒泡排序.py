"""
author: Lns-XueFeng
CreateTime: 2023.03.23
"""

"""冒泡排序
扫描一个列表n次, 每次顺序扫描过去对于每相邻的两元素进行排序, 
即, 每扫描一个列表一次, 便找到了一个最大值, 相当于维护了一个子有序列表在最右端

标准定义：冒泡排序需要多次遍历列表, 
它比较相邻的项并交换那些无序的项,
每次遍历列表将下一个最大的值放在其正确的位置
"""


def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(li)
print(li)


# 优化：如果列表已然有序, 第一次遍历完成便可以退出
def short_bubble_sort(a_list):
    pass_num = len(a_list) - 1
    while pass_num > 0:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        if exchanges:
            break
        pass_num = pass_num - 1


li = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(li)
print(li)
