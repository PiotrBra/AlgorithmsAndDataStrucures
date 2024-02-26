from zad7testy import runtests
from math import inf
"""
przechodze po kolumnach najpierw w dol a potem w wyznaczajac najwieksza odleglosc od DP[0][0] i zwracam odleglosc DP[n-1][n-1]
zlozonosc algorytmu O(n^2)
"""




def maze( L ):
    n = len(L)
    DP = [[-inf for _ in range(n)] for _ in range(n)]
    DP[0][0] = 0

    for i in range(1, n):
        if L[i][0] == '#':
            break
        DP[i][0] = i
    for j in range(1, n):
        down = [-inf] * n
        up = [-inf] * n
        for i in range(n):
            if L[i][j] == '#':
                continue
            if(i == 0):
                if(L[i][j-1] != '#'):
                    down[i] = DP[i][j-1] + 1
            else:
                if(L[i][j-1] != '#'):
                    down[i] = DP[i][j-1] + 1
                down[i] = max(down[i], down[i-1]+1)
        for i in range(n-1, -1, -1):
            if(L[i][j] == '#'):
                continue
            if (i == n-1):
                if (L[i][j - 1] != '#'):
                    up[i] = DP[i][j - 1] + 1
            else:
                if (L[i][j-1] != '#'):
                    up[i] = DP[i][j - 1] + 1
                up[i] = max(up[i], up[i+1] + 1)
        for k in range(n):
            DP[k][j] = max(up[k], down[k])

    if DP[n-1][n-1] != -inf:
        return DP[n-1][n-1]
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )