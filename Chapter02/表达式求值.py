"""
author: Lns-XueFeng
CreateTime: 2023.03.02
"""


"""表达式求值
利用计算机解决 A+B*C 这样的中缀表达式计算
1.人为转换成全括号表达式 (A+(B*C))
    将表达式转换为全括号表达式的关键点在于
    让程序根据运算符的优先级来添加括号
    
    1.从左往右扫描
    2.如果是运算数则(A入栈
    3.如果遇到运算符，则判断，如果是低优先级运算符则入栈，如果是高优先级运算符则入栈该运算符，并标记下一次遇到的运算数也需入栈并且入栈)
    4.最后通过count计算还需入栈几个右括号)
    
    2.读取两个字符，如果有运算符，左边加上左括号，入栈
    3.如果再次读取的两个字符中的运算符优先级大于之前的，左边加上括号，入栈
    3.如果无法读入两个字符，即最后一个字符了，则入栈，并根据前面加上括号的次数n，右括号入栈n次
    
2.设计算法将全括号表达式转换成后缀表达式或前缀表达式
    将运算符移动到离他最近的左括号对应的右括号的右边
    去除表达式中的括号，即可得到后缀表达式，前缀表达式同理
    
    1.从左往右扫描，
    2.如果是左括号和字母则入栈1，
    3.如果遇到运算符就入栈2，
    4.如果遇到右括号则压入栈1且弹出栈2中的运算符入栈1
    
3.设计算法计算后缀表达式
    后缀表达式特性也符合栈的反转特性，离字母越近的运算级越优先
    
    1.从左往右扫描
    2.如果是字母则入栈1
    3.如果是运算符，则弹出栈1中的两个元素进行运算，再入栈1
    4.最后栈中会剩余一个元素，就是结果
    
以上思考规划肯定是会有纰漏的地方，因此，当写完之后要测试不同情况，然后修改代码，直至完美运行
"""


from stack import Stack


def convert(expression: str):
    """输入表达式，输出全括号表达式"""
    s = Stack()
    ex_list = list(expression)
    length = len(ex_list)
    index = 0   # 列表元素索引
    count = 0   # 计算最后需要入栈的)数量， 最终要为零
    next_enter_stack = False
    while ex_list:
        if index >= length:   # 循环退出条件
            if count > 0:
                s.push(")")
                count = count - 1
                continue
            break
        ex = ex_list[index]
        if next_enter_stack:
            s.push(ex)
            s.push(")")
            count = count - 1
            next_enter_stack = False
            index = index + 1
            continue
        if ex not in "+-*/":
            s.push("(")
            s.push(ex_list[index])
            count = count + 1
        if ex in "+-*/":
            if ex in "+-":
                s.push(ex)
            if ex in "*/":
                next_enter_stack = True
                s.push(ex)
        index = index + 1
    return s.items()


def operation(expression: str):
    """输入全括号表达式，输出后缀表达式"""
    s1 = Stack()
    s2 = Stack()
    # alphabet = "ABCDEFGHIZKLMNOPQRSTUVWEXYZ"
    for ex in expression:
        if ex not in "+-*/)":
            s1.push(ex)
        if ex in "+-*/":
            s2.push(ex)
        if ex == ")":
            s1.push(ex)
            s1.push(s2.pop())
    while not s2.isEmpty():
        s1.push(s2.pop())   # 测试时发现：加入防止s2中留有运算符

    new_expression = ""
    for i in s1.items():
        if i not in "()":
            new_expression += i
    return new_expression


def calculate_expression(expression: str):
    """输入后缀表达式，输出后缀表达式计算值"""
    s1 = Stack()
    # alphabet = "ABCDEFGHIZKLMNOPQRSTUVWEXYZ"
    for ex in expression:
        if ex not in "+-*/":
            s1.push(ex)
        if ex in "+-*/":
            t1, t2 = s1.pop(), s1.pop()
            s1.push(do_operate(int(t1), int(t2), ex))
    return s1.pop()


def do_operate(t1: int, t2: int, ex: str):
    """输入：两个数字 运算方式， 输出它们的计算结果"""
    if ex == "+":
        return t1 + t2
    if ex == "-":
        return t2 - t1   # 测试时发现：8-1会被变成1-8，因此先简单的将这里反转一下
    if ex == "*":
        return t1 * t2
    if ex == "/":
        return t2 / t1   # 测试时发现：8/1会被变成1/8，因此先简单的将这里反转一下


if __name__ == "__main__":
    # print(operation("(A+((B*C)+(D*F)))"))
    # print(operation("(1+((2*2)+(2*2)))"))
    # print(calculate_expression(operation("(1+((2*2)+(2*2)))")))
    entire_expression = convert("1+2*3+4*5+1+8/1")
    suffix_expression = operation(entire_expression)
    calculate_value = calculate_expression(suffix_expression)
    print(calculate_value)
