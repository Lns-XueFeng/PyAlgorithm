"""
author: Lns-XueFeng
CreateTime: 2023.05.01
"""


# 图Graph是一种比树更为一般的结构，也是由节点和边构成
# 比如图可以用来表示道路交通路线系统...


# 邻接矩阵实现图数据结构
# 但现实中的用图来表示的数据结构基本都是稀疏的, 因此邻接矩阵过于浪费空间, 邻接列表是更好的选择


# 邻接列表实现图数据结构
# 维护一个包含图中所有节点的主列表, 主列表中的每个顶点再关联一个与自身有边连接的所有顶点的列表


class Graph:
    def __init__(self, vertices, edges, directed=False):
        self.vertices = vertices
        self.edges = edges
        self.directed = directed
        self.adj_matrix = self.build_adj_matrix()
        self.adj_list = self.build_adj_list()

    def build_adj_matrix(self):
        n = len(self.vertices)
        adj_matrix = [[0] * n for _ in range(n)]
        for edge in self.edges:
            i, j = edge
            adj_matrix[i][j] = 1
            if not self.directed:
                adj_matrix[j][i] = 1
        return adj_matrix

    def build_adj_list(self):
        adj_list = [[] for _ in range(len(self.vertices))]
        for edge in self.edges:
            i, j = edge
            adj_list[i].append(j)
            if not self.directed:
                adj_list[j].append(i)
        return adj_list


vertices = [0, 1, 2, 3]
edges = [(0, 1), (0, 3), (2, 1)]
graph = Graph(vertices, edges)
print(graph.adj_matrix)
print(graph.adj_list)
