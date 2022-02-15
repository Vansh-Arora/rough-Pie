def DFShelper(V,adj,node,ans):
        V[node] = 1
        ans.append(node)
        for i in adj[node]:
            if V[i] == 0:
                DFShelper(V,adj,i)

def DFS(adj,V):
    visi = [0 for i in range(V)]
    ans = []
    count = 0
    for i in range(V):
        if visi[i] == 0:
            count += 1
            DFShelper(visi,adj,i,ans)
    print("Connected Components = {}".format(count))



# [[1, 2], [0, 3, 4, 5, 6], [0, 6], [1], [1], [1], [1, 2]]
adjList = [[1, 2], [0, 3, 4, 5, 6], [0, 6], [1], [1], [1], [1, 2], [8, 9], [7], [7], [11], [10]]
DFS(adjList,12)
