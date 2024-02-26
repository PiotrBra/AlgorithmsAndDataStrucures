from collections import deque
from math import inf

def SCC_matrix(G):
    visited = [False for _ in range(len(G))]
    color = [None for _ in range(len(G))]
    stack = deque()

    def SCC_matrix_util(G, visited, stack, u):
        visited[u] = True

        for v, edge in enumerate(G[u]):
            if not visited[v] and edge == 1:
                SCC_matrix_util(G, visited, stack, v)
        stack.append(u)

    def Cut(G, visited, color, u, component):
        visited[u] = True
        color[u] = component
        for v in range(len(G)):
            if not visited[v] and G[v][u] == 1:
                Cut(G, visited, color, v, component)

    for i in range(len(G)):
        if not visited[i]:
            SCC_matrix_util(G, visited, stack, i)

    for i in range(len(G)):
        visited[i] = False

    component = 0
    while stack:
        u = stack.pop()
        if not visited[u]:
            Cut(G, visited, color, u, component)
            component += 1
    return color


def SCC_list(G):
    visited = [False for _ in range(len(G))]
    color = [None for _ in range(len(G))]
    stack = deque()

    def SCC_list_util(G, visited, stack, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                SCC_list_util(G, visited, stack, v)
        stack.append(u)

    def Cut(G, visited, color, u, component):
        visited[u] = True
        color[u] = component
        for v in G[u]:
            if not visited[v]:
                Cut(G, visited, color, v, component)

    for i in range(len(G)):
        if not visited[i]:
            SCC_list_util(G, visited, stack, i)

    H = [[] for _ in range(len(G))]
    for i in range(len(G)):
        visited[i] = False

    for u, edges in enumerate(G):
        for v in edges:
            H[v].append(u)

    component = 0
    while stack:
        u = stack.pop()
        if not visited[u]:
            Cut(H, visited, color, u, component)
            component += 1
    return color
