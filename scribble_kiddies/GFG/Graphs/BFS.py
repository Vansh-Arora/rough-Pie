# It works only for connected graph.
def BFS(adj,V):
    visi = [0 for i in range(V)]
    q = []
    level = [0 for i in range(V)]
    top = -1
    end = -1
    q.append(0)
    level[0] = 0
    visi[0] = 1
    top += 1
    end += 1
    while top <= end:
        cur = q[top]
        top += 1
        for i in adj[cur]:
            if not visi[i]:
                level[i] = level[cur]+1
                visi[i] = 1
                q.append(i)
                end += 1
    print(level)
    return q






adjList = [[1, 2], [0, 3, 4, 5, 6], [0, 6], [1], [1], [1], [1, 2], [8, 9], [7], [7], [11], [10]]
BFS(adjList,12)