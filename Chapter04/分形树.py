"""
author: Lns-XueFeng
CreateTime: 2023.03.14
"""


# 分形树
def tree(n):
    if n > 0:   # 退出条件
        turtle.forward(n)
        turtle.right(30)
        tree(n - 15)
        turtle.left(60)
        tree(n - 15)
        turtle.right(30)
        turtle.backward(n)


if __name__ == "__main__":
    import turtle
    turtle.right(90)
    turtle.penup()
    turtle.forward(150)
    turtle.pendown()
    turtle.left(180)
    tree(75)
    turtle.mainloop()
