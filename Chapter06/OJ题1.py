"""
author: Lns-XueFeng
CreateTime: 2023.03.30
"""


"""
著名的快速排序算法里有一个经典的划分过程：
我们通常采用某种方法取一个元素作为主元（中值），通过交换，把比主元小的元素放到它的左边，比主元大的元素放到它的右边
给定划分后的N个互不相同的非负整数的排列，请问有多少个元素可能是划分前选取的主元？
例如给定的排列是[1, 3, 2, 4, 5]。则：
1 的左边没有元素，右边的元素都比它大，所以它可能是主元
尽管 3 的左边元素都比它小，但其右边的 2 比它小，所以它不能是主元
尽管 2 的右边元素都比它大，但其左边的 3 比它大，所以它不能是主元
类似原因，4 和 5 都可能是主元。因此，有 3 个元素可能是主元

输入：一行数个整数的排列，由空格分隔
输出：在第 1 行中输出有可能是主元的元素个数
在第 2 行中按递增顺序输出这些元素，其间以 1 个空格分隔，行首尾不得有多余空格（若元素个数为0则第二行为一行空行）。
"""


def find_pivot(nums):
    n = len(nums)
    left_max = [0] * n
    right_min = [float('inf')] * n
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], nums[i - 1])
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], nums[i + 1])
    res = []
    for i in range(n):
        if left_max[i] < nums[i] < right_min[i]:
            res.append(nums[i])
    print(len(res))
    print(' '.join(map(str, res)))


find_pivot([1, 3, 2, 4, 5])
