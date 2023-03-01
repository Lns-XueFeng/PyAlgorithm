"""
author: Lns-XueFeng
CreateTime: 2023.03.01
"""


"""
括号匹配问题：判断一个字符串中的括号是否是对齐的，即()or{}or[]等
比如：((({{{[[[[]]]]}}})))
观察这个字符串，会发现其是居中对齐匹配的括号，特征符合“反转次序”，适合用栈来解决！

思路：
循环判断字符串，如果是左括号则入栈，
否则弹出栈顶元素与当前循环元素比较，
如果相同则证明匹配，如果不相同则之间return False表示不匹配
如果循环顺利结束，表示均匹配，那么最后判断栈是否为空，如果为空则return True，否则return False

注意测试：左边括号多的情况，右边括号多的情况，中间不同括号的插入情况.
"""

from stack import Stack


def matches(string):
    bracket_stack = Stack()
    left_bracket_dict = {"(": 1, "{": 2, "[": 3}
    right_bracket_dict = {")": 1, "}": 2, "]": 3}

    for s in string:
        if s in "({[":
            bracket_stack.push(s)
        if s in ")}]":
            if not bracket_stack.isEmpty():
                temp = bracket_stack.pop()
                if left_bracket_dict[temp] != right_bracket_dict[s]:
                    return False
            else:
                return False

    if bracket_stack.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    words = "((({{{[[[[人生苦短，我用Python]]]]}}})))"
    if matches(words):
        print("此字符串括号均成对")
    else:
        print("此字符串括号有不成对的")
