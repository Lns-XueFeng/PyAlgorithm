"""
author: Lns-XueFeng
CreateTime: 2023.03.01
"""


"""
十进制整数转换成二进制数
一直除以2得到的余数最终要倒着连起来，与栈的反转特性相匹配，故可利用栈来解决此问题

思路：利用2整除法，不断地将十进制数进行除2，利用%得得其每次的余数，直至该数为0或1.

然后将十进制转化为二进制的，扩展成任意base
"""


from stack import Stack


def convert(number, base):
    s = Stack()
    digits = "0123456789ABCDEF"

    while number > 1:
        remainder = number % base
        s.push(remainder)
        number = number // base
    s.push(number)

    b_num = ""
    while not s.isEmpty():
        b_num = b_num + digits[s.pop()]
    return b_num


if __name__ == "__main__":
    b_number = convert(100, 2)
    print(b_number)
