from collections import deque
from copy import deepcopy
def bfss(g1, g2, s, t, parent):
    visited = [False] * len(g1)
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()

        for v in range(len(graph)):
            if not visited[v] and g2[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True

    return False

def bfs(g,g2, s, t, parent):
    q = deque()
    vis = [False] *len(g)
    vis[s] = True
    q.append(s)
    while q:
        u = q.popleft()
        for v in range(len(g)):
            if not vis[v] and g2[u][v] > 0:
                parent[v] = u
                vis[v] = True
                q.append(v)
                if v == t: return True
    return False

def ford_fulkerson(g, s, t):
    parent = [-1] * len(g)
    max_flow = 0
    g2 = deepcopy(g)
    while bfs(g, g2, s, t, parent):
        path_flow = float('inf')
        v = t

        while v != s:
            u = parent[v]
            path_flow = min(path_flow, g2[u][v])
            v = u

        v = t

        while v != s:
            u = parent[v]
            g2[u][v] -= path_flow
            g2[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow


graph = [[0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0]]

source = 0
sink = 5

max_flow = ford_fulkerson(graph, source, sink)
print("Maksymalny przepływ w grafie wynosi:", max_flow)