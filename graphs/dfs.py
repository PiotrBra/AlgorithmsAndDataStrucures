def DFS_list(G, s=0):

    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = [0 for _ in range(len(G))]
    T = 0


    def DFS_list_util(G, visited, parent, time, u):
        nonlocal T
        time[u] = T
        T += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_list_util(G, visited, parent, time, v)

    DFS_list_util(G, visited, parent, time, s)

    for i in range(len(G)):
        if not visited[i]:
            DFS_list_util(G, visited, parent, time, i)

    print("LIST")
    print("time from ", s, ": ")
    print(time)
    print("parents: ")
    print(parent)


def DFS_matrix(G, s=0):
    def DFS_matrix_util(G, visited, parent, time, u):
        nonlocal T
        time[u] = T
        T += 1
        visited[u] = True
        for v, edge in enumerate(G[u]):
            if not visited[v] and edge == 1:
                parent[v] = u
                DFS_matrix_util(G, visited, parent, time, v)

    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = [0 for _ in range(len(G))]
    T = 0

    DFS_matrix_util(G, visited, parent, time, s)



def DFS(G):
    vis = [False] * len(G)
    par = [None] * len(G)
    time = 0
    def DFSvis(G,u):
        nonlocal time
        time +=1
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                par[v] = u
                DFSvis(G,v)
        time += 1
        for u in range(len(G)):
            if not vis[u]:
                DFSvis(G, u)





