"""
author: Lns-XueFeng
CreateTime: 2023.03.13
"""


def convert(number, base):
    convert_table = "0123456789ABCDEF"
    if number < base:
        return convert_table[number]
    return convert(number // base, base) + convert_table[number % base]   # 这里的+号表示的是连接


convert(10, 2)   # 1010

# 和Chapter02”进制转换.py“对比
# 建议打个断点，debug去看执行情况，变量情况，栈中的情况

"""
比如以上述代码为例，在第8行打断点进行debug
不断的单步执行看变量变化情况，执行情况，栈的情况
一直到进入递归退出条件，继续点单步调试，看返回的情况

从退出递归开始，栈中弹出：
convert(1 // 2, 2) 的值为 convert_table[1]   -> 1
convert(2 // 2, 2) 的值为 convert(1 // 2, 2) + convert_table[2 % 2]   -> 10
convert(5 // 2, 2) 的值为 convert(2 // 2, 2) + convert_table[5 % 2]   -> 101
convert(10 // 2, 2) 的值为 convert(5 // 2, 2) + convert_table[10 % 2]   -> 1010
弹出结束，最终结果为：1010

调用顺序：convert(10 // 2, 2) -> convert(5 // 2, 2) -> convert(2 // 2, 2) -> convert(1 // 2, 2)
返回顺序：convert(1 // 2, 2) -> convert(2 // 2, 2) -> convert(5 // 2, 2) -> convert(10 // 2, 2)
“递归”与“返回” 又称 “递归”与“回溯”

将调用的四个函数做编号4、3、2、1
解决问题的思路就是，”不断的分解问题为更小规模的相同问题直至基本相同问题“，这样解决了1就能解决2就能解决3最终解决4
"""
