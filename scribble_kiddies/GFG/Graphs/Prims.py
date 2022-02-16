def Prims(V,adj):
    cost = [9999 for i in range(V)]
    minTree = [0 for i in range(V)]
    res = 0
    for count in range(V):
        u = -1
        for i in range(V):
            if mTree[i] == 0 and (u == -1 or cost[i]<cost[u]):
                u = i
        minTree[u] = 1
        res = res + cost[u]
        for k in range(V):
            if minTree[k] == 0 and adj[u][k] != 0 and adj[u][k] < cost[k]:
                cost[k] = adj[u][k]
    return res
