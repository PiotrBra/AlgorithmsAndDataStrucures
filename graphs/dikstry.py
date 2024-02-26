from _collections import deque
from math import inf
#(V+E)logV
def relax(par,d,v,c,u):
    if d[v] > d[u] + c:
        d[v] = d[u] + c
        par[v] = u
        return True
    return False


def dijskry(g,a):# O(ElogV)
    n = len(g)
    d = [inf for _ in range(n)]
    par = [None for _ in range(n)]
    d[a] = 0
    q = deque()
    q.append((d[a],a))
    while q:
        w,u = q.popleft()
        if w == d[u]:
            d[u] = w
            for v,c in g[u]:
                  if relax(par,d,v, c, u):
                      q.append((d[v],v))
    return d