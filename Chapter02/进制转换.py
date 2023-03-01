"""
author: Lns-XueFeng
CreateTime: 2023.03.01
"""


"""
十进制整数转换成二进制数
一直除以2得到的余数最终要倒着连起来，与栈的反转特性相匹配，故可利用栈来解决此问题

思路：利用2整除法，不断地将十进制数进行除2，利用%得得其每次的余数，直至该数为0或1.
"""


from stack import Stack


def convert(number):
    s = Stack()
    while number > 1:
        remainder = number % 2
        s.push(remainder)
        number = number // 2
    if number == 0 or number == 1:
        s.push(number)

    b_num = ""
    while not s.isEmpty():
        b_num = b_num + str(s.pop())
    return b_num


if __name__ == "__main__":
    b_number = convert(100)
    print(b_number)
