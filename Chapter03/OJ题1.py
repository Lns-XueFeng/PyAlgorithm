"""
author: Lns-XueFeng
CreateTime: 2023.03.09
"""


"""
一开始给出了一个由小写字母组成的字符串 S
我们规定每次移动中，选择最左侧的字母，将其从原位置移除，并加到字符串的末尾。这样的移动可以执行任意多次
返回我们移动之后可以拥有的最小字符串（注：在Python3中，字符串的大小可用不等号比较）

代码模板(建议复制粘贴使用)：
def func(S):
    # your code here
    return output
    
S = input()
print(func(S))

输入
S, S为仅含有小写字母的字符串，长度不超过100000
输出
一个与S等长的字符串
"""


from queue_ import Queue


def get_small_str(string: str):
    queue = Queue()
    for st in string:
        queue.enqueue(st)

    min_string = "".join(queue.items())
    for _ in range(queue.size()-1):
        queue.enqueue(queue.dequeue())
        temp = "".join(queue.items())
        if temp < min_string:
            min_string = temp

    return min_string


if __name__ == "__main__":
    S = input()
    print(get_small_str(S))
