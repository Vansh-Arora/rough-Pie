def DFShelper(V,adj,node,R):
    V[node] = 1
    R[node] = 1
    for i in adj[node]:
        if V[i] == 0 and DFShelper(V,adj,i,R):
            return 1
        elif R[i] == 1:
            return 1
    R[node] = 0
    return 0


def DFS(adj,V):
    visi = [0 for i in range(V)]
    rec = [0 for i in range(V)]
    for i in range(V):
        if not visi[i]:
            if DFShelper(visi,adj,i,rec):
                return 1
    return 0

adjList = [[1, 2], [3, 4, 5, 6], [6], [], [], [], []]
ans = DFS(adjList,7)
print(ans)
