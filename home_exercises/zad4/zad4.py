#Piotr Branewski
from zad4testy import runtests
from collections import deque
"""
algorytm za pomocą BFS wyszukuje nakrótszą scieżkę z s do t,
nastepnie w pętli która przechodzi po kolojenych wierzcholkach w tej scieżce usuwa krawędź
i sprawdza BFS'em czy najrótsza scieżka się powiększyła. jesli tak to zwracam x,y jesli nie to None
złożoność algorytmu to O(n(V+E)) gdzie n = najkrótsza scieżka. 
"""



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
        if d[t] == -1:
            return(x, y)
        y = x
        x = par[y]
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )