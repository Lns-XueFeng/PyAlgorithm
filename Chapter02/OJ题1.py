"""
author: Lns-XueFeng
CreateTime: 2023.03.03
"""


"""OJ题1：有效的括号
题目：
    给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。
    有效字符串需满足：
    1.左括号必须用相同类型的右括号闭合。
    2.左括号必须以正确的顺序闭合。
    3.注意空字符串可被认为是有效字符串。
    
输入格式:
    一行字符串
输出格式：
    True或False，表示该输入是否为合法括号串
    
思路：
    建立一个栈，从左往右扫描字符串
    如果是左括号，则入栈
    如果是右括号，则弹出栈顶元素，进行判断，如果匹配则下一个循环，如果不匹配则return False
    如果扫描顺利扫描完成，则检查栈是否为空，为空则说明此字符串括号匹配
    
    忘记考虑空字符串也为有效字符串了
    
最后测试不同情况用例
"""


from stack import Stack


def match(string: str):
    if len(string.strip()) == 0:
        return True

    s = Stack()
    bracket_dict = {"(": 1, "{": 2, "[": 3, ")": 1, "}": 2, "]": 3}
    for st in string:
        if st in "({[":
            s.push(st)
        if st in ")}]":
            if not s.isEmpty():
                if bracket_dict[st] != bracket_dict[s.pop()]:
                    return False
            else:
                return False
    if not s.isEmpty():
        return False
    return True


if __name__ == "__main__":
    print(match("({[]})}])"))
