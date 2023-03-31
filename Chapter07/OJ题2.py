"""
author: Lns-XueFeng
CreateTime: 2023.03.31
"""


"""描述
给定一个列表与数字K，按出现次数倒序输出列表中前K个出现最频繁的元素；
若少于K个元素则返回所有元素。若有两个或以上的元素出现次数相等，按元素的值进行顺序输出，小的在前。
参考代码模板：
def topKFrequent(nums, k):
    # code here
    pass

lst = eval(input())
k = int(input())
topKFrequent(lst, k)
"""


def top_k_frequent(nums, k):
    dic = {n: 0 for n in set(nums)}
    for n in nums:
        if n in dic:
            dic[n] = dic[n] + 1
    sort_dic = sorted(dic.items(), key=lambda d: (-d[1], d[0]))
    if len(sort_dic) > k:
        return [n[0] for n in sort_dic[:k]]
    return [n[0] for n in sort_dic]


# lst = eval(input())
# k = int(input())
print(*top_k_frequent([2, 1, 1, 1, 2, 2, 3], 2))
