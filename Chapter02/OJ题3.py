"""
author: Lns-XueFeng
CreateTime: 2023.03.03
"""


"""OJ题3：强迫症老板和他的洗碗工
题目：
    洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，
    并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。
    小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。
    老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，
    这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。你也能像老王一样作出准确的判断吗？
    
输入：
    长度为10的字符串，其中只包含0～9的数字，且不重复，代表顾客依次取到的盘子编号
输出：
    字符串：Yes或者No，表示遵照次序洗盘子，或者没有遵照次序洗盘子
    
思路：
    如果桌子上没碗，栈为空，则洗碗工洗一个盘子，入栈
    然后反复的问，有没有人要拿的是这个碗啊！如果有，出栈，下一个人，如果还是有那就重复此流程，
    直到为空或者是没人要则洗下一个碗,并继续上一流程
    最后如果栈中无碗了，则返回True，否则返回False
"""


from stack import Stack


def match(string: str):
    s = Stack()
    index = 0
    count_take = 0   # 当前排队的人（第几个）
    for c in list("0123456789"):
        if index == 0:
            s.push(c)
        if not s.isEmpty():
            if s.see_top() == string[count_take]:
                s.pop()
                count_take += 1
                while not s.isEmpty():
                    if s.see_top() == string[count_take]:
                        s.pop()
                        count_take += 1
                        continue
                    break
        if index != 0:
            s.push(c)
        index += 1

    if not s.isEmpty():
        while not s.isEmpty():
            if s.see_top() == string[count_take]:
                s.pop()
                count_take += 1
                continue
            break

    if not s.isEmpty():
        return False
    return True


if __name__ == "__main__":
    print(match("0123456789"))
