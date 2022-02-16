def isCyclic(V, adj):
    # code here
    indi =[0 for i in range(V)]
    for i in range(V):
        for j in adj[i]:
            indi[j] += 1
    q = []
    top = -1
    end = -1
    for i in range(V):
        if indi[i] == 0:
            q.append(i)
            if top == -1:
                top += 1
            end += 1
    count = 0
    while top <= end and end > -1:
        cur = q[top]
        top += 1
        count += 1
        for i in adj[cur]:
            indi[i] -= 1
            if indi[i] == 0:
                q.append(i)
                end += 1
    if count == V:
        return 0
    return 1