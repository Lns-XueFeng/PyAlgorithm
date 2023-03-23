"""
author: Lns-XueFeng
CreateTime: 2023.03.21
"""


# dp1中的示例解决的是“重复子问题”
# dp2将展示解决的是“最优组合问题”


"""最少硬币找零
25美分、10美分、1美分, 利用这三种进行硬币找零
比如给1美元购买37美分找零, 最少的是两个25美分, 一个10美分和三个1美分
"""


# 贪婪方法：尽可能的用最大的硬币, 然后再去找下一个小点的硬币, 并尽可能多的使用它们, 这就是贪婪策略
def eager():
    pass


"""然而这样呢?
25美分、21美分、10美分、1美分, 利用这三种进行硬币找零
比如给1美元购买37美分找零, 最少的是三个21美分
"""


# 暴力递归
def recMC(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            numCoins = 1 + recMC(coin_value_list, change - i)
            if numCoins < min_coins:
                min_coins = numCoins
    return min_coins


recMC([1, 5, 10, 25], 63)


# 记忆化递归
def recDC(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            numCoins = 1 + recDC(coin_value_list, change - i,
                                 known_results)
            if numCoins < min_coins:
                min_coins = numCoins
                known_results[change] = min_coins
    return min_coins


recDC([1, 5, 10, 25], 63, [0] * 64)


# 动态规划
def dpMakeChange(coin_value_list, change, min_coins):
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coinCount:
                coinCount = min_coins[cents - j] + 1
        min_coins[cents] = coinCount
    return min_coins[change]


# 动态规划解题框架
# 若确定给定问题具有重叠子问题和最优子结构, 那么就可以使用动态规划求解, 总体上看, 求解可分为四步：
# 1.状态定义：构建问题最优解模型, 包括问题最优解的定义, 有哪些计算解的自变量
# 2.初始状态：确定基础子问题的解(即已知解), 原问题和子问题的解都是以基础子问题的解为起始点, 在迭代计算中得到的
# 3.转移方程：确定原问题的解与子问题的解之间的关系是什么, 以及使用何种选择规则从子问题最优解组合中选出原问题最优解
# 4.返回值：确定应返回的问题的解是什么, 即动态规划在何处停止迭代


"""斐波那契数列
1.状态定义：一维dp列表, 设第i个斐波那契数列为dp[i]
2.初始状态：已知第0和第1个斐波那契数, dp[0]=0, dp[1]=1
3.转移方程：从第三个开始, 后一个数是前两个数之和, 即dp[i] = dp[i-1] + dp[i-2]
4.返回值：返回dp[i]
"""

"""找零问题

"""