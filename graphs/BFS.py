from collections import deque
#v+e
def BFS_list(G, s):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = [0 for _ in range(len(G))]
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()
        for v in G[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                time[v] = time[u] + 1
    return time

#v^2
def BFS_matrix(G, s):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = [0 for _ in range(len(G))]
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()
        for v, edge in enumerate(G[u]):
            if not visited[v] and edge == 1:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                time[v] = time[u] + 1
    return time