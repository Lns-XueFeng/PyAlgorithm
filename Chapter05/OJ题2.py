"""
author: Lns-XueFeng
CreateTime: 2023.03.25
"""


"""题目内容：
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分
你需要按照以下要求，帮助老师给这些孩子分发糖果：每个孩子至少分配到 1 个糖果
相邻的孩子中，评分高的孩子必须获得更多的糖果。那么这样下来，老师至少需要准备多少颗糖果呢？

输入：一个列表，以文本格式的有效Python表达式给出

输出：一行数字，表示满足分配条件所需的最少糖果数
"""


def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)


if __name__ == "__main__":
    print(candy([1, 2, 2]))
