"""
author: Lns-XueFeng
CreateTime: 2023.03.16
"""


"""
描述：
谢尔宾斯基地毯一种正方形分形图案，每个地毯可分为等大小的9份，其中中央挖空，其余均由更小的地毯组成。
现给定地毯大小（行数）与组成地毯的字符元素，请打印相应的地毯图形。
注：空腔以半角空格表示；当给定字符元素长度不为1时空格数须与字符长度对应

输入：
输入为两行，分别为地毯大小正整数N与组成元素字符串c
输入数据保证N为3的正整数幂

输出：
由N行长度为N*len(c)的字符串构成的谢尔宾斯基地毯

思路：
第一先根据题意给的输入输出, 得到一个矩阵, 这样便可以通过列表api进行操作
第二步递归实现谢尔斯基地毯
第三步将地毯矩阵格式化打印出来
"""


def get_two_dim(n, char):
    """根据输入3的次幂输出一个矩阵"""
    two_dim_li = []
    row_count = 0
    for _ in range(n):
        row_li = []
        col_count = 0
        for _ in range(n):
            if row_count == 0 or row_count == n-1:
                row_li.append(char)
            else:
                if col_count == 0 or col_count == n-1:
                    row_li.append(char)
                else:
                    row_li.append("  ")
            col_count += 1
        two_dim_li.append(row_li)
        row_count += 1
    return two_dim_li


def ascii_div_shape(n, char, matri):
    """利用递归实现ascii谢尔斯基地毯"""
    def check(n, x, y):
        if n <= 1:
            return True
        m = n // 3
        if m <= x < m * 2 and m <= y < m * 2:
            return False
        return check(m, x % m, y % m)

    for x in range(n):
        for y in range(n):
            if check(n, x, y):
                matri[x][y] = char
            else:
                matri[x][y] = "  "
    return matri


def format_print(two_dim_li):
    """格式化打印矩阵, 使其在终端输出和题目输出一致"""
    for row in two_dim_li:
        for v in row:
            print(v, end='')
        print('')


import pprint
pprint.pprint(get_two_dim(9, "[]"))   # 利用pprint能更加美观的打印
print()
format_print(get_two_dim(9, "[]"))
print()


n = int(input())   # 只能为3的次幂
char = input()   # 例如[]
matrix = get_two_dim(n, char)
format_print(ascii_div_shape(n, char, matrix))
