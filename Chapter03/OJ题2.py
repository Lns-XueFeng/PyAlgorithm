"""
author: Lns-XueFeng
CreateTime: 2023.03.11
"""


"""
计算每个事件发生之时，往前算10000毫秒内有多少个事件发生，包含当事件；
也即对于列表中的每个元素k，算出整个列表中有多少个元素介于k-10000和k（两端均含）之间。

代码模板(建议复制粘贴使用)：
def func(mylist):
    # your code here
    return output
    
mylist = eval(input())
print(func(mylist))

输入
一个已排序列表mylist，所有元素为非负整数，记录各个请求的发生时间，单位为毫秒。

输出
一个与mylist等长的列表。
"""

from collections import deque


def func(mylist):
    output = []
    dq = deque()

    i = 0
    while i < len(mylist):
        dq.append(mylist[i])
        while len(dq) > 0 and mylist[i] - dq[0] > 10000:
            dq.popleft()
        j = i + 1
        while j < len(mylist) and mylist[j] == mylist[i]:
            dq.append(mylist[j])
            j += 1
        while i < j:
            output.append(len(dq))
            i += 1
    return output


if __name__ == "__main__":
    mylist = input()
    print(func(mylist))
