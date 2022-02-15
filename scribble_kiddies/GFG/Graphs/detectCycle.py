def detectCycle(V,adj,node,p):
    V[node] = 1
    for i in adj[node]:
        if V[i] == 0:
            if detectCycle(V,adj,i,node) == 1:
                return 1
        elif i != p:
            return 1
    return 0


def DFS(adj,V):
    visi = [0 for i in range(V)]
    for i in range(V):
        if visi[i] == 0:
            if detectCycle(visi,adj,i,-1):
                return 1
    return 0


#[[1],[0, 2],[1]]
# [[1, 2], [0, 3, 4, 5, 6], [0, 6], [1], [1], [1], [1, 2]]
adjList = [[1, 2], [0, 3, 4, 5, 6], [0], [1], [1], [1], [1], [8, 9], [7], [7], [11], [10]]
ans = DFS(adjList,12)
print(ans)
