import math


class Graph:
    def __init__(self, directed=False, ):
        self.directed = directed
        self.edges = {}
    
    def add_v(self, v: str):
        if v not in self.edges:
            self.edges[v] = {}

    def add_edge(self, edge: tuple[str, str], weight: int=1):
        self.add_v(edge[0])
        self.add_v(edge[1])

        self.edges[edge[0]][edge[1]] = weight

        if not self.directed:
            self.edges[edge[1]][edge[0]] = weight
    
    def get_neighbors(self, v: str):
        return self.edges.get(v, {})
    
    def get_neigh_list(self, v: str):
        neigh = []
        for i in self.get_neighbors(v):
            neigh.append(i)
        return neigh


def get_ways(G: Graph, s: str, t: str, way=None):
    if way is None:
        way = [s]
    else:
        way = way + [s]

    if s == t:
        return [way]
    
    ways = []
    for i in G.get_neigh_list(s):
        if i not in way:
            next = get_ways(G, i, t, way)
            ways.extend(next)
    
    return ways


def get_zhegalkin_polynomial(f: list[int], var: list[str]):
    result_list = [f[0]]
    polynomial = ""
    if f[0] == 1:
        polynomial += "1"

    while len(f) > 1:
        for i in range(len(f) - 1):
            f[i] = (f[i] + f[i + 1]) % 2
        result_list.append(f[0])
        f.pop(-1)
    
    for i in range(1, len(result_list)):
        if result_list[i] == 1:
            bi = bin(i)[2:].zfill(len(var))
            conjunct = ""
            for j in range(len(var)):
                conjunct += var[j] * int(bi[j])
            polynomial += f" + {conjunct}"

    return polynomial


def get_func_count(_class: str, n: int):
    if _class == "T0" or _class == "T1":
        return 2 ** (2 ** n - 1)
    elif _class == "S":
        return 2 ** (2 ** (n - 1))
    elif _class == "L":
        return 2 ** (n + 1)
    elif _class == "M":
        """Невозможно?"""
        count_dict: dict = {1: 3,
                            2: 6,
                            3: 20,
                            4: 168,
                            5: 7581}
        return count_dict[n]


def get_shortest_ham_cycle(G):
    """
    Получает на вход матрицу смежности, где для взвешенных графов
    в i,j позиции находится вес ребра (i, j)

    Возвращает длину кратчайшего гамильтонова цикла(если есть)
    """

    n = len(G)
    visited = [0] * n
    visited[0] = 1
    min_len = [math.inf]

    def passing(cur, count, lenght):
        if count == n:
            if G[cur][0] != math.inf:
                min_len[0] = min(min_len[0], lenght + G[cur][0])
            return 

        for i in range(n):
            if not visited[i]:
                if G[cur][i] != math.inf:
                    visited[i] = 1
                    passing(i, count + 1, lenght + G[cur][i])
                    visited[i] = 0
        
    passing(0, 1, 0)
    
    return min_len[0]
