"""
author: Lns-XueFeng
CreateTime: 2023.04.09
"""


"""树的应用：
程序的编译：先将源代码解析成语法树->再利用语法树转换成机器代码

这里以表达式解析为例：
"""


class Stack:
    def __init__(self):
        self.__items = []   # 规定列表左边为栈底，右边为栈顶

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def isEmpty(self):
        return len(self.__items) == 0

    def items(self):
        return self.__items


class BinaryTree:
    top = ""

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        temp_l = None
        if self.left_child is not None:
            temp_l = "not None"
        temp_r = None
        if self.right_child is not None:
            temp_r = "not None"
        return f"key: {self.key} left: {temp_l} right: {temp_r}"

    def insert_left(self, new_node):
        temp_tree = BinaryTree(new_node)
        if self.left_child is None:
            self.left_child = temp_tree
        else:
            temp_tree.left_child = self.left_child
            self.left_child = temp_tree

    def insert_right(self, new_node):
        temp_tree = BinaryTree(new_node)
        if self.right_child is None:
            self.right_child = temp_tree
        else:
            temp_tree.right_child = self.right_child
            self.right_child = temp_tree

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_value(self, value):
        self.key = value

    def get_root_value(self):
        return self.key


def build_parse_tree(fp_exp: str) -> BinaryTree:
    """ 解析全括号表达式 """
    fp_list = fp_exp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for e in fp_list:
        if e == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif e not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_value(e)
            parent = p_stack.pop()
            current_tree = parent
        elif e in ['+', '-', '*', '/', ')']:
            current_tree.set_root_value(e)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif e == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree


def evaluate(parse_tree: BinaryTree):
    """ 计算全表达式解析树 """
    import operator
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        fn = opers[parse_tree.get_root_value()]
        return fn(evaluate(left_child), evaluate(right_child))
    return parse_tree.get_root_value()


print(evaluate(build_parse_tree("((3+2)*(2+3))")))
