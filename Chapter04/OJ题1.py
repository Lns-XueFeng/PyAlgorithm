"""
author: Lns-XueFeng
CreateTime: 2023.03.16
"""


"""
题目内容：
给定一个M进制的数，请将其转换为N进制并输出

输入：
两行，第一行为空格分隔的两个数字，分别为10进制表示的M与N；其中M, N均满足2 ≤ M、N ≤ 36
第二行为待转换的M进制数字，其中每位超过9的部分从10至36分别用大写字母A-Z表示；输入数据保证数据的每一位不超过M

输出：
一行字符串，表示转换后的N进制数

例如：
2 10
1010
输出其十进制形式：10

思考：
对于输入M进制的数，将其转化为十进制数
而后再将十进制的数转换为N进制的数

吐槽：
那个测试系统, 我input加个提示, 它就给我不过......
"""


def any_to_ten(m, m_num):
    """迭代实现：任意进制的数->十进制数"""
    search_table = "0123456789ABCDEFGHIZKLMNOPQRSTUVWXYZ"
    m_num = str(m_num)
    length = len(m_num)
    result = 0
    for i in m_num:
        length = length - 1
        result = result + (m ** length) * search_table.index(i)
    return result


def r_any_to_ten(m, m_num):
    """递归实现：任意进制的数->十进制数"""
    search_table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m_num = str(m_num)
    length = len(m_num)
    length = length - 1
    if length < 1:
        return search_table.index(m_num[0]) * (m ** length)
    return search_table.index(m_num[0]) * (m ** length) + r_any_to_ten(m, m_num[1:])


def ten_to_any(num, n):
    """十进制数->任意进制数"""
    search_table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num < n:
        return search_table[num]   # base case
    return ten_to_any(num // n, n) + search_table[num % n]


def any_convert(m, n, m_num):
    result = r_any_to_ten(m, m_num)
    return ten_to_any(result, n)


if __name__ == "__main__":
    M_N_li = input("从M进制转到N进制：").split()   # input提示在提交OJ时去掉, 否则一直报错不给过
    converted_num = input("需被转换的M进制的数：")   # input提示在提交OJ时去掉, 否则一直报错不给过
    print(any_convert(int(M_N_li[0]), int(M_N_li[1]), converted_num))
