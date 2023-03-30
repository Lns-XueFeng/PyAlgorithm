"""
author: Lns-XueFeng
CreateTime: 2023.03.25
"""


"""题目内容：
给定一个表达式字符串，求出按不同的求值顺序可能得到的所有结果
示例代码模板：
def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    # code here

expr=input()
print(findWays(expr))

输入：一行字符串，仅包含0-9与运算符+、-与*

注：字符串保证三种运算符左右均为数字字符

输出：所有不重复的可能的结果，从小到大排序并以半角逗号","分隔
"""


def findWays(expr):
    # 用于将字符串转为数字与运算符，供参考
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)

    def helper(nums, ops):
        if not ops:
            return [nums[0]]
        res = []
        for i in range(len(ops)):
            left = helper(nums[:i+1], ops[:i])
            right = helper(nums[i+1:], ops[i+1:])
            for l in left:
                for r in right:
                    if ops[i] == '+':
                        res.append(l + r)
                    elif ops[i] == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)
        return res

    return ",".join([str(i) for i in sorted(list(set(helper(nums, ops))))])


expr = input()
print(findWays(expr))


