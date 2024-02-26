#Piotr Branewski
from collections import deque
from zad5testy import runtests
"""
Algorytm tworzy nowy graf z krawędziami podanymi w E oraz z krawędziami z S o wart. 0.
Następnie za pomocą algorytmu dijskry wylicza najkrotszą scieżkę i zwaraca.
Złożoność: O(nlogm + n ) gdzie n = liczba krawedzi, m = liczba wierzcholkow
"""
def relax(par,d,v,c,u):
    if d[v] > d[u] + c:
        d[v] = d[u] + c
        par[v] = u
        return True
    return False


def dijskry(g,a):# O(ElogV)
    n = len(g)
    d = [float("inf") for _ in range(n)]
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


def spacetravel( n, E, S, a, b ):
    G: list[list[tuple]] = [[] for _ in range(n)]
    for i in range(len(S)-1):
        E.append((S[i],S[i+1],0))
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1], E[i][2]))
        G[E[i][1]].append((E[i][0], E[i][2]))
    d = dijskry(G,a)
    if d[b] != float("inf"):
        return d[b]
    else:
        return None
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )

