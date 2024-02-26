from collections import deque
def longer( G, s, t ):
    def bfs(g, s):
        q = deque()
        n = len(g)
        d = [-1 for v in range(n)]
        vis = [False for v in range(n)]
        par = [None for v in range(n)]
        d[s] = 0
        vis[s] = True
        par[s] = None
        q.append(s)
        while q:
            u = q.popleft()
            for v in g[u]:
                if not vis[v]:
                    d[v] = d[u] + 1
                    par[v] = u
                    vis[v] = True
                    q.append(v)
        return d, par
    d, par = bfs(G,s)
    min = d[t]
    x = par[t]
    y = t
    while x is not None:
        A = G
        A[x].remove(y)
        d = bfs(A, s)[0]
        if d[t] > min:
            return (x, y)
        y = x
        x = par[y]
    return None


def bfs(g, s):
    q = deque()
    n = len(g)
    d = [-1 for v in range(n)]
    vis = [False for v in range(n)]
    par = [None for v in range(n)]
    d[s] = 0
    vis[s] = True
    par[s] = None
    q.append(s)
    while q:
        u = q.popleft()
        for v in g[u]:
            if not vis[v]:
                d[v] = d[u] + 1
                par[v] = u
                vis[v] = True
                q.append(v)
    return d, par
g = [[0,1],[0,2],[1,2]]
print(longer(g,0,2))
