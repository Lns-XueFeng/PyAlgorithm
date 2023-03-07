"""
author: Lns-XueFeng
CreateTime: 2023.03.07
"""


# 双端队列这种数据结构适用于”判断回文字“这种类型的问题
# 例如判定”ABCDCBA“、”上海自来水来自海上“是不是回文字


"""思路
1.首先将需要判定的字符串加入双端队列
2.接着同一时刻从双端队列的两端取出元素进行比较
3.如果相同，则进行下一次，否则return False
4.重复2、3步直至双端队列仅剩一个元素，return True
"""


from deque_ import Deque


def judge(string: str):
    deque = Deque()
    for st in string:
        deque.add_front(st)

    while deque.length() > 1:
        front_item = deque.remove_front()
        rear_item = deque.remove_rear()
        if front_item != rear_item:
            return False
    return True


if __name__ == "__main__":
    need_judge_str = "上海自来水来自海上"
    result = judge(need_judge_str)
    print(f"”{need_judge_str}“是回文字：{result}")

