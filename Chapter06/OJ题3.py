"""
author: Lns-XueFeng
CreateTime: 2023.03.30
"""


"""描述
给出如下定义：
插入排序是迭代算法，逐一获得输入数据，逐步产生有序的输出序列。每步迭代中，算法从输入序列中取出一元素，将之插入有序序列中正确的位置
如此迭代直到全部元素有序
归并排序进行如下迭代操作：首先将原始序列看成 N 个只包含 1 个元素的有序子序列，然后每次迭代归并两个相邻的有序子序列
直到最后只剩下 1 个有序的序列
现给定原始序列和由某排序算法产生的中间序列，请你判断该算法究竟是哪种排序算法？

输入样例：
3 1 2 8 7 5 9 4 0 6
1 3 2 8 5 7 4 9 0 6

输出样例：
Merge Sort
1 2 3 8 4 5 7 9 0 6

输入样例2：
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0

输出样例2：
Insertion Sort
1 2 3 5 7 8 9 4 6 0

输入：两行由空格分隔的数字，其对应长度相等的列表
其中第一行代表未排序的列表，第二行是排序算法过程中某一步的中间列表

输出：首先在第 1 行中输出Insertion Sort表示插入排序、或Merge Sort表示归并排序
然后在第 2 行中输出用该排序算法再迭代一轮的结果序列。题目保证每组测试的结果是唯一的。数字间以空格分隔，且行首尾不得有多余空格
"""


def judge_sort(nums, mid_nums):
    n = len(nums)
    if mid_nums[:n-1] == sorted(mid_nums[:n-1]):
        print('Insertion Sort')
        for i in range(n-1, 0, -1):
            if mid_nums[i] < mid_nums[i-1]:
                mid_nums[i], mid_nums[i-1] = mid_nums[i-1], mid_nums[i]
            else:
                break
        print(' '.join(map(str, mid_nums)))
    else:
        print('Merge Sort')
        k = 2
        while all(mid_nums[i:i+k] == sorted(mid_nums[i:i+k]) for i in range(0, n, k)):
            k *= 2
        k *= 2
        for i in range(0, n, k):
            mid_nums[i:i+k] = sorted(mid_nums[i:i+k])
        print(' '.join(map(str, mid_nums)))


nums = list(map(int, input().split()))
mid_nums = list(map(int, input().split()))
judge_sort(nums, mid_nums)
