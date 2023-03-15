"""
author: Lns-XueFeng
CreateTime: 2023.03.16
"""

"""汉诺塔: |杆子, -盘子
  |    |    |
  |    |    |
  -    |    |
 ---   |    |
-----  |    |
  a    b    c
要将a上三个盘子挪到c上
可以先将前3-1个盘子挪到c上, 再挪到b上, 然后将3-2个盘子挪到c, 最后将b上3-1个盘子挪到c上
而对于如何将前两个盘子挪到b上, 将第一个盘子挪到c, 第二个盘子挪到b, 第一个盘子从c挪到b

而挪动这两个盘子的方法适用于这个问题的任何规模, 因此对于N个盘子
将N-1个盘子从a挪到c, 从c挪到b, 将a上第N个盘子从a挪到c, 将b上N-1个盘子从b挪到c
"""


def move_disk(disk, begin_pole, end_pole):
    print(f"Moving disk[{disk}] from {begin_pole} to {end_pole}")


def move_tower(height, begin_pole, middle_pole, end_pole):
    """以三个举例
    将height-1个从a->c->b, 交换end_pole, middle_pole, 然后move_disk从a->b, 完成第一步
    递归调用解决两个盘子, 交换end_pole, middle_pole, 然后move_disk从a->c, 完成第二步
    递归调用解决一个盘子, 交换begin_pole, middle_pole, 然后move_disk从b->c, 完成第三步
    """
    if height >= 1:
        move_tower(height - 1, begin_pole, end_pole, middle_pole)   # 交换middle_pole与end_pole
        move_disk(height, begin_pole, end_pole)   # 这样a才能到b, 完成第一步, 这是第一次回溯
        move_tower(height - 1, middle_pole, begin_pole, end_pole)   # 交换


move_tower(3, "a", "b", "c")
