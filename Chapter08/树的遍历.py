"""
author: Lns-XueFeng
CreateTime: 2023.04.09
"""


"""树的遍历：
前序遍历：先访问根节点, 在递归的前序访问左子树、最后前序访问右子树
中序遍历：先递归的中序访问左子树, 在访问根节点, 最后中序访问右子树
后序遍历：先递归的后序访问左子树, 再后序访问右子树, 最后访问根节点
"""


# 前序遍历
def preorder(tree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


# 中序遍历
def inorder(tree):
    if tree is not None:
        preorder(tree.get_left_child())
        print(tree.get_root_value())
        preorder(tree.get_right_child())


# 后序遍历
def postorder(tree):
    if tree is not None:
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
        print(tree.get_root_value())
