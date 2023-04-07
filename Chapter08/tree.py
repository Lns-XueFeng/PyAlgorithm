"""
author: Lns-XueFeng
CreateTime: 2023.04.07
"""


# 树的定义1：树由若干节点，以及两两连接节点的边组成
# 树的定义2：树是空集或者由根节点及0或多个子树构成，每个子树的根到根节点具有边相连


# 链表法实现树
class BinaryTree:
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


binary_tree = BinaryTree('a')
binary_tree.insert_left('b')
binary_tree.insert_right('c')
binary_tree.get_right_child().set_root_value("Hello")
binary_tree.get_left_child().insert_right('d')

print(binary_tree.get_left_child())
print("-" * 80)


# 嵌套列表法实现树
"""
每个列表都是[root, left, right]
进行层层嵌套实现递归定义的树

很容易扩展成多叉树
比如[root, first, second, three]，即为三叉树
"""


class BinaryRtree:
    def __init__(self, root):
        self.root = [root, [], []]

    def __repr__(self):
        return f"BinaryRtree: {self.root}"

    def insert_left(self, new_branch):
        left_branch = self.root.pop(1)
        if left_branch is None:
            self.root.insert(1, [new_branch, [], []])
        else:
            self.root.insert(1, [new_branch, left_branch, []])

    def insert_right(self, new_branch):
        right_branch = self.root.pop(2)
        if right_branch is None:
            self.root.insert(2, [new_branch, [], []])
        else:
            self.root.insert(2, [new_branch, [], right_branch])

    def get_left_child(self, tree):
        return tree[1]

    def get_right_child(self, tree):
        return tree[2]

    def set_root_value(self, tree, value):
        tree[0] = value

    def get_root_value(self, tree):
        return tree[0]


binary_rtree = BinaryRtree(3)
binary_rtree.insert_left(4)
binary_rtree.insert_left(5)
binary_rtree.insert_right(6)
binary_rtree.insert_right(7)
tree_li = binary_rtree.root
left_child = binary_rtree.get_left_child(tree_li)
print(left_child)

binary_rtree.set_root_value(left_child, 9)
print(binary_rtree)

binary_rtree.insert_left(11)
print(binary_rtree)
tree_li = binary_rtree.root
print(binary_rtree.get_right_child(binary_rtree.get_right_child(tree_li)))
