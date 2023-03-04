"""
author: Lns-XueFeng
CreateTime: 2023.03.03
"""


"""OJ题2：一维开心消消乐
问题：
    开心消消乐我们都熟悉，
    我们可以用刚学过的栈来做一个“一维”的开心消消乐游戏，
    这个游戏输入一串字符，逐个消去相邻的相同字符对。
    如果字符全部被消完，则输出不带引号的“None”

输入格式:
    一个字符串，可能带有相邻的相同字符，如“aabbbc”
输出格式：
    一个字符串，消去了相邻的成对字符，如“bc”
    
思路：”消除相邻的成对的相同字符串“
    因此可以扫描字符串，如果栈为空，则压入，否则比对
    如果此字母与当前栈顶字母是否相同，相同则此字母不入栈，否则入栈
    扫描完成之后，如果栈为空则返回None，否则遍历栈将字符连接起来，注意顺序
    
最后测试不同情况用例
"""


from stack import Stack


def remove_same_char(string: str):
    s = Stack()
    index = 0
    str_length = len(string)
    while index < str_length:
        if index == 0:
            s.push(string[index])
            index = index + 1
            continue
        if not s.isEmpty():
            if string[index] != s.see_top():
                s.push(string[index])
                index = index + 1
            else:
                s.pop()   # 如果相同则消去
                index = index + 1
                continue
        else:
            s.push(string[index])
            index = index + 1
    if s.isEmpty():
        return None

    re_string = []
    while not s.isEmpty():
        st = s.pop()
        re_string.insert(0, st)

    string = "".join(re_string)
    return string


if __name__ == "__main__":
    print(remove_same_char("beepooxxxyz"))
