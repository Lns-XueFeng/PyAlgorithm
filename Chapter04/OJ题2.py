"""
author: Lns-XueFeng
CreateTime: 2023.03.16
"""


"""
描述：
如课上所说，汉诺塔问题源于印度一个古老传说。对于原始的汉诺塔游戏，可供玩家操作的空间一共只有三根柱子，导致按原传说的要求，需要超过1.8*10^19步才能解开。
透过新增柱子可以大幅度地减少需要的步数。此处要求在给出指定的盘数，柱子数量为4（即限制为4根柱子）且不改变原有传说的其他规则的限制下，找出完成迁移的最小步骤数。

输入：
一个非负整数M，M代表盘数，M<=1000。
输出：
一个非负整数，表示完成迁移的最小步骤数。

别人的思路：
首先三柱汉诺塔问题的最优解次数g(n) = 2^n -1（已经证明），设四柱汉诺塔问题 的最优解次数为f(n)
接着将四柱汉诺塔问题分为三步来解，设有a,b,c,d四个柱子，a柱子上有n个盘子：
1.将a柱上的 x个盘子(1<= x < n)，移动到c柱上，这个过程可以使用b柱和d柱，所以这是一个四柱汉诺塔问题，最优次数为f(x)
2.将a柱上剩下的n-x个盘子移动到d柱，因为剩下的盘子都比c柱上现有的盘子多，所以只能通过b柱来移动，这是一个三柱汉诺塔问题，最优次数为 2^(n-x) - 1
3.最后将c柱上的x个盘子移动到d柱即可，可以通过a，b柱来移动，所以是一个四柱汉诺塔问题，和第一步相同最优次数为f(x)
所以四柱汉诺塔问题需要的总次数f(n) = f(x) + 2^(n-x) - 1 + f(x) =2* f(x) + 2^(n-x) -1,最优次数与x的取值有关，易求得 f(1) = 1；f(2) = 3, 可以用循环遍历来找f(n)的最小值

本质还是数学归纳法
"""


def move_disk(disk, a, c):
    global step
    step = step + 1
    print(f"Moving disk[{disk}] from {a} to {c}")


def hanoi(height, a, b, c):
    if height > 0:
        hanoi(height - 1, a, c, b)
        move_disk(height, a, c)
        hanoi(height - 1, b, a, c)


step = 0
hanoi(3, 'a', 'b', 'c')
print(f"所用的步骤：{step}")


def four_hanoi(num1):
    ans = []
    if num1 == 1:   # base case
        return [1]
    if num1 == 2:   # base case
        return ans_list
    if num1-1 > len(ans_list):
        four_hanoi(num1 - 1)   # 递进

    for i in range(1, num1):
        ans.append(2 * ans_list[i-1] + 2 ** (num1 - i) - 1)
    ans_list.append(min(ans))
    return ans_list[-1]


ans_list = [1, 3]
min_step = four_hanoi(int(input()))
print(min_step)
