from copy import deepcopy

def Euler_cycle_matrix(G):
    def Is_eulerian(G):
        for i in range(len(G)):
            degree = 0
            for j in range(len(G)):
                if G[i][j] == 1:
                    degree += 1
            if degree % 2 == 1:
                return False
        return True

    if not Is_eulerian(G):
        print("Graph isn't Eulerian")
        return

    H = deepcopy(G)

    def Euler_cycle_matrix_util(u):
        nonlocal H
        print(u)
        for v in range(len(H)):
            if H[u][v] == 1:
                H[u][v] = 0
                H[v][u] = 0
                Euler_cycle_matrix_util(v)

    Euler_cycle_matrix_util(0)


def Euler_cycle_list(G):
    def Is_eulerian(G):
        for i in range(len(G)):
            if len(G[i]) % 2 == 1:
                return False
        return True