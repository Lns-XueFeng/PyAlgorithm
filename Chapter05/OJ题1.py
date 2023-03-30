"""
author: Lns-XueFeng
CreateTime: 2023.03.25
"""


"""题目内容：
给定一个长度为N的区域，及4种不同长度的瓷砖：
灰瓷砖（长为1格）、红瓷砖（长为2格）、绿瓷砖（长为3格）与蓝瓷砖（长为4格），求所有不同的铺满整个区域的方法数

输入：一个非负整数N

输出：一行数字，表示不同的方法总数
"""


def tile_ways(N):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in [1, 2, 3, 4]:
            if i - j >= 0:
                dp[i] += dp[i - j]
    return dp[N]


if __name__ == "__main__":
    print(tile_ways(5))
