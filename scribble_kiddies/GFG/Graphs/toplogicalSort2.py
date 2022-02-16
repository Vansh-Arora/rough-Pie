def DFSr(V,adj,st,node):
    V[node] = 1
    for i in adj[node]:
        if not V[i]:
            DFSr(V,adj,st,i)
    st.append(node)



def DFS(V,adj):
    visi  = [0 for i in range(V)]
    st = []
    for i in range(V):
        if visi[i] == 0:
            DFSr(visi,adj,st,i)
    st.reverse()
    for i in range(V-1,-1,-1):
        print(st[i])

adjList = [[1, 2], [3, 4, 5, 6], [6], [], [], [], []]
DFS(7,adjList)