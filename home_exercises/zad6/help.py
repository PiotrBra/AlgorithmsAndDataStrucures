def bpm(g, u, matchR, seen):
    # Try every job one by one
    for v in range(len(g)):

        # If applicant u is interested
        # in job v and v is not seen
        if g[u][v] and seen[v] == False:

            # Mark v as visited
            seen[v] = True

            if matchR[v] == -1 or bpm(g, matchR[v], matchR, seen):
                matchR[v] = u
                return True
    return False


# Returns maximum number of matching
def maxBPM(g):
    matchR = [-1] * len(g)

    # Count of jobs assigned to applicants
    result = 0
    for i in range(len(g)):

        # Mark all jobs as not seen for next applicant.
        seen = [False] * len(g)

        # Find if the applicant 'u' can get a job
        if bpm(g,i, matchR, seen):
            result += 1
    return result


g =[[0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1]]
print(maxBPM(g))

def BFSs(g, s, t, parent):
    queue = deque()
    visited = [False] * len(g)
    result = []
    queue.appendleft(s)
    visited[s] = True
    while not queue:
        u = queue.pop()
        result.append(u)
        for v in range(len(g)):
            if visited[v] is False and g[u][v] == 1:
                queue.appendleft(v)
                visited[v] = True
                parent[v] = u
                if v==t:
                    return True
    return False

def bfs(g,g2, s, t, parent):
    q = deque()
    vis = [False] *len(g)
    vis[s] = True
    q.append(s)
    while q:
        u = q.popleft()
        for v in range(len(g)):
            if not vis[v] and g2[u][v] > 0:
                parent[v] = u
                vis[v] = True
                q.append(v)
                if v == t: return True
    return False

def ford_fulkerson(g, s, t):
    parent = [-1] * len(g)
    max_flow = 0
    g2 = deepcopy(g)
    while bfs(g,g2, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, g2[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            g2[u][v] -= path_flow
            g2[v][u] += path_flow
            v = u
        max_flow += path_flow
    return max_flow