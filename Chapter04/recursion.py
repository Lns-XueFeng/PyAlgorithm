"""
author: Lns-XueFeng
CreateTime: 2023.03.13
"""

"""递归三定律
1.递归算法必须调用自身（函数）
2.递归算法必须有一个基本的结束条件（边界）
3.递归算法必须能够改变自身的状态向基本条件演进（递推公式）

首先明确函数的功能作用是什么，确定函数的参数，确定函数返回值
其次是明确与写出递归的边界条件，正确的退出递归，避免无限递归
最后是确定递推公式，逐渐减少算法的规模或让输入的值尽可能的靠近临界值
"""

# 递归调用的本质 --> 数学归纳法 --> 将一个大问题分解成若干个小问题来解决

"""递归适用于哪些问题？
递归算法一般用于解决三类问题：
1问题解的定义是按递归定义的（代表有阶乘、斐波那契数列）
2问题解法由回溯算法实现（如数字排列组合问题）
3数据的结构形式是按递归定义的（树的遍历，图的搜索、嵌套列表）
"""


# 数列求和
def sum_(li):
    if len(li) == 1:  # 递归退出条件
        return li[0]  # 基本问题
    return li[0] + sum_(li[1:])  # 通过调用自身解决规模更小的问题


sum_([1, 2, 3, 4, 5])  # result->15


# 反转字符串
def reverse_(st):
    if len(st) <= 1:
        return st[0]
    return reverse_(st[1:]) + st[0]


reverse_("abcdefg")  # result->gfedcba


# 阶乘
def factorial(num):
    if num <= 1:
        return num
    return num * factorial(num - 1)


factorial(4)  # result->24


# 斐波那契数列
# 斐波纳契数列，又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、……
# 输入n输出第n个数
def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


fib(5)  # result->5


# 全排列
# 从n个不同元素中任取m（m≤n）个元素，按照一定的顺序排列起来
# 叫做从n个不同元素中取出m个元素的一个排列。当m=n时所有的排列情况叫全排列
def perm(num_li, start, end):
    if start == end:
        all_li.append(num_li)
        return

    for i in range(start, end):
        num_li[start], num_li[i] = num_li[i], num_li[start]   # 交换
        perm(num_li, start+1, end)
        num_li[start], num_li[i] = num_li[i], num_li[start]   # 换回来


all_li = []
v_li = [1, 2, 3]
perm(v_li, 0, len(v_li))
print(all_li)

