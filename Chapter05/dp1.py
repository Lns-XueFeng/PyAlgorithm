"""
author: Lns-XueFeng
CreateTime: 2023.03.21
"""


"""动态规划
动态规划就是：给定一个问题, 我们把他拆成一个子问题, 直到子问题可以直接解决
然后把子问题的答案保存起来, 以减少重复计算, 再根据子问题答案反推, 得出原问题解的一种方法
"""


# 动态规划包含了分治思想、空间换时间、最优解等多种基石算法
# 分治思想：通过将原问题分解为子问题, 不断递归的将子问题分解为更小的子问题, 并通过组合子问题的解来得到原问题的解
# 动态规划：其也是通过组合子问题得到原问题的解, 不同的是适合用动态规划解决的问题具有"重叠子问题"和"最优子结构"两大特性
# 找到"重叠子问题"和"最优子结构"可通过画分支图


# 例如解决斐波那契数列

# 暴力递归
def fib1(n):
    if n <= 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


fib1(100)

"""暴力递归
这是斐波那契数列的暴力递归解法, 
非常简洁直观, 但是如果我们去画分支图, 
会发现做了非常多的重复计算, 这大大增加的时间复杂度2的n次方
因此可以每计算出一个新的结果, 便保存起来, 如果后面又遇到就直接拿此结果
"""


# 记忆化递归
def fib2(n, temp):
    if n <= 2:
        return 1
    if n in temp:   # 每次计算前查询字典, 看是否已经有结果了
        return temp[n]
    temp[n] = fib2(n - 1, temp) + fib2(n - 2, temp)   # 将计算得到的值存入字典
    return temp[n]   # 再将存入字典的值返回


temp_memo1 = {}
fib2(100, temp_memo1)

"""记忆化递归
如果你运行fib1(100), 会运算非常久, 
但是如果你运行fib2(100), 直接就得出结果,
其原因就是, 通过缓存遇到重复的直接查询得到结果, 无需计算,
但是fib2终究还是递归的, 反复的调用函数的开销非常大,
因此咱们尝试将记忆化递归改成非递归形式
"""


# 非递归形式
def fib3(n):
    if n == 0:
        return 0
    rn1, rn2 = 0, 1
    for i in range(2, n+1):
        rn1, rn2 = rn2, rn1 + rn2
    return rn2


temp_memo2 = {}
fib3(100)

"""
记忆化递归和动态规划的本质思想是一致的, 是对斐波那契数列定义的不同表现形式
记忆化递归 — 从顶至低, 动态规划 — 从底至顶
"""


"""总结：
比如解决斐波那契数列：
    -我们写出的算法：暴力递归 -> 大量重复计算
    -可进行记忆化：记忆化递归 -> 用空间换时间
    -修改为非递归：动态规划 -> 转换为非递归, 好算复杂度以及省去函数开辟消耗
"""