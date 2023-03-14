"""
author: Lns-XueFeng
CreateTime: 2023.03.14
"""


import turtle


# 绘制一个三角形
def draw_triangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    # 绘制左边
    myTurtle.goto(points[1][0], points[1][1])
    # 绘制右边
    myTurtle.goto(points[2][0], points[2][1])
    # 绘制底边
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


# 用于获取两个点的中间点
def get_middle(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


#  points表示当前绘制的大三角形的三个顶点，degree表示当前阶数，必须大于0，才继续绘制，myTurtle是还会作图对象
def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'yellow', 'white', 'orange']

    # 绘制大三角形，从颜色列表中根据degree选择一种颜色
    draw_triangle(points, colormap[degree - 1], myTurtle)

    if degree > 0:
        # 绘制左下角三角形
        sierpinski([points[0], get_middle(points[0], points[1]), get_middle(points[0], points[2])],
                   degree - 1,
                   myTurtle)
        # 绘制上方的三角形
        sierpinski([points[1], get_middle(points[0], points[1]), get_middle(points[1], points[2])],
                   degree - 1,
                   myTurtle)
        # 绘制右下角三角形
        sierpinski([points[2], get_middle(points[2], points[1]), get_middle(points[0], points[2])],
                   degree - 1,
                   myTurtle)


if __name__ == "__main__":
    myTurtle = turtle.Turtle()
    window = turtle.Screen()
    points = [[-200, -100], [0, 200], [200, -100]]
    sierpinski(points, 5, myTurtle)
    window.exitonclick()
