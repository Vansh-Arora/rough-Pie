def indeg(adj,V):
    inD = [0 for i in range(V)]
    for i in range(V):
        for j in adj[i]:
            inD[j] += 1
    return inD


def topo(adj,V,inD):
    q = []
    top = -1
    end = -1
    for i in range(V):
        if inD[i] == 0:
            q.append(i)
            if top == -1:
                top += 1
            end += 1
    while top <= end:
        cur = q[top]
        top += 1
        for i in adj[cur]:
            inD[i] -= 1
            if inD[i] == 0:
                q.append(i)
                end += 1
    return q


adjList = [[1, 2], [3, 4, 5, 6], [6], [], [], [], []]
inD = indeg(adjList,7)
print(topo(adjList,7,inD))