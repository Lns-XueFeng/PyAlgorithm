"""
author: Lns-XueFeng
CreateTime: 2023.03.16
"""

import turtle


# 迷宫类
class Maze(object):
    # 读取迷宫数据，初始化迷宫内部，并找到海龟初始位置。
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)
        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze / 2
        self.yTranslate = rowsInMaze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-columnsInMaze / 2, -rowsInMaze / 2, columnsInMaze / 2,
                                    rowsInMaze / 2)

    # 在屏幕上绘制迷宫
    def drawMaze(self):
        self.t.speed(20)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'orange')

    # 画方块
    def drawCenteredBox(self, x, y, color):
        self.t.up()  # 画笔抬起
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor('green')
        self.t.setheading(90)  # 设置海龟的朝向, 标准模式：0-东, 90-北, 180-西, 270-南 logo模式：0-北, 90-东, 180-南, 270-西
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    # 移动海龟
    def moveTurtle(self, x, y):
        self.t.up()  # 画笔抬起
        self.t.setheading(self.t.towards(x + self.xTranslate,
                                         -y + self.yTranslate))
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)

    # 画路径圆点
    def dropBreadcrumb(self, color):
        self.t.dot(color)

    # 用以更新迷宫内的状态及在窗口中改变海龟位置，行列参数为乌龟的初始坐标。
    def updatePosition(self, row, col, val):
        self.mazelist[row][col] = val  # 设置该标记状态为当前单元格的值
        self.moveTurtle(col, row)  # 移动海龟
        if val == PART_OF_PATH:  # 其中一条成功路径的圆点的颜色
            color = 'green'
        elif val == TRIED:  # 尝试用的圆点的颜色
            color = 'black'
        elif val == DEAD_END:  # 死胡同用的圆点的颜色
            color = 'red'
        self.dropBreadcrumb(color)  # 画路径圆点并上色

    # 用以判断当前位置是否为出口。
    def isExit(self, row, col):
        return row == 0 or row == self.rowsInMaze - 1 or col == 0 or col == self.columnsInMaze - 1

    # 返回键对应的值，影响searchFrom()中maze[startRow][startColumn]值的获取
    def __getitem__(self, key):
        return self.mazelist[key]


# 探索迷宫，注意此函数包括三个参数：一个迷宫对象、起始行、起始列
def searchFrom(maze, startRow, startColumn):
    # 1. 遇到障碍
    if maze[startRow][startColumn] == OBSTACLE:
        return False

    # 2. 发现已经探索过的路径或死胡同
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False

    # 3. 发现出口
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True

    maze.updatePosition(startRow, startColumn, TRIED)

    # 4. 依次尝试每个方向
    found = searchFrom(maze, startRow - 1, startColumn) or \
        searchFrom(maze, startRow + 1, startColumn) or \
        searchFrom(maze, startRow, startColumn - 1) or \
        searchFrom(maze, startRow, startColumn + 1)

    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)  # 返回其中一条正确路径
    else:  # 4个方向均是死胡同, 四个均为false
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


if __name__ == '__main__':
    PART_OF_PATH = 'O'  # 部分路径
    TRIED = '.'
    OBSTACLE = '+'
    DEAD_END = '-'  # 死胡同
    myMaze = Maze('map.txt')
    myMaze.drawMaze()
    searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
