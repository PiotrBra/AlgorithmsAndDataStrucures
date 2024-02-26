from zad8testy import runtests


def plan(T):
    n = len(T)
    m = len(T[0])
    ropa = T[0][0]
    for i in range(1,n):
        if T[i][0] == 0:
            break
        for j in range(m):
            if T[i][j]:
                ropa+=T[i][j]


    return ropa


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = False )

