"""
author: Lns-XueFeng
CreateTime: 2023.03.30
"""


"""描述：
现在有同一个产品的N个版本，编号为从1至N的整数；其中从某个版本之后所有版本均已损坏。
现给定一个函数isBadVersion，输入数字N可判断该版本是否损坏（若损坏将输出True）；请找出第一个损坏的版本。
注：有时isBadVersion函数运行速度很慢，请注意优化查找方式

输入：两行
第一行为整数，为产品号总数N
第二行为给定的判断函数，使用有效的Python表达式给出，可使用eval读取

输出：一行数字，表示第一个损坏的版本
"""


N = int(input())
isBadVersion = eval(input())


def firstBadVersion(N):
    left, right = 1, N
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left


print(firstBadVersion(N))
