#Piotr Branewski
from zad6testy import runtests
"""
Algorytm polega na tym, że tworzę nowy graf w postaci macierzowej w ktorym sa osoby i maszyny. 
nastepnie odpalam algorytm na najwieksze skojarzenie  i zwracam wynik.
zlozonosc algorytmu to O(2E + VlogE)
"""

def dfsrec(g, u, par, vis):
    for v in range(len(g)):
        if g[u][v] and vis[v] == False:
            vis[v] = True
            if par[v] == -1 or dfsrec(g, par[v], par, vis):
                par[v] = u
                return True
    return False


def maxskojarzenie(g):
    par = [-1] * len(g)
    result = 0
    for i in range(len(g)):
        vis = [False] * len(g)
        if dfsrec(g,i, par, vis):
            result += 1
    return result


def binworker( M ):
    n = len(M)
    G = [[0 for _ in range(2 * n)] for _ in range(2 * n)]
    for i in range(n):
        for j in range(len(M[i])):
            G[i][M[i][j] + n] = 1
    return maxskojarzenie(G)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
