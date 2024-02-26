from math import inf

def Edges(G):
    for index, neighbours in enumerate(G):
        for destination, weight in neighbours:
            yield index, destination, weight


# O( V * E )
def Bellman_ford(G, s):
    distance = [inf for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    distance[s] = 0

    edges = 0
    for i in range(len(G)):
        edges += len(G[i])

    for i in range(len(G) - 1):
        #        for index, neighbours in enumerate(G):
        #            for u, weight in neighbours:
        for i in range(edges):
            for v, u, weight in Edges(G):
                if distance[v] != inf and distance[u] > distance[v] + weight:
                    distance[u] = distance[v] + weight
                    parent[u] = v