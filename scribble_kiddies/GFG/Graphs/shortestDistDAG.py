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
def sho(q,adj,w):
    dist = [999 for i in range(len(adj))]
    dist[q[0]] = 0
    for i in q:
        for j in adj[i]:
            #print("{}: {} {}: {} w[i][j]: {}".format(i,dist[i],j,dist[j],w[i][j]))
            if dist[j] > dist[i] + w[i][j]:
                dist[j] = dist[i] + w[i][j]
    return dist




adj = [[1,4], [2], [3], [], [2, 5], [3]]

ind = indeg(adj,len(adj))
q = topo(adj, len(adj), ind)









w = []
for i in range(6):
    w.append([])
    for j in range(6):
        w[i].append(-1)

w[0][1] = 2
w[0][4] = 1
w[1][2] = 3
w[4][2] = 2
w[4][5] = 4
w[5][3] = 1
w[2][3] = 6

print(sho(q,adj,w))
