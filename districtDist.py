def BFS(adj,V,H,level,visi):
    q = []
    #level = [0 for i in range(V)]
    top = 0
    end = -1
    for i in H:
        q.append(i)
        end += 1
        visi[i] = 1
        level[i] = 0

    while top <= end:
        cur = q[top]
        top += 1
        for i in adj[cur]:
            if not visi[i]:
                visi[i]=1
                level[i]  = level[cur]+1

                
                q.append(i)
                end += 1

    return level





def solution(N, A, B, H):
    # write your code in Python 3.6
    adj = [[] for i in range(N)]
    visi = [0 for i in range(N)]
    level = [float('inf') for i  in range(N)]
    roads = len(A)
    for i in range(roads):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
    
    for i in range(N):
        if len(adj[i]) == 0:
            if i not in H:
                return -1
    

    ans = BFS(adj,len(adj),H,level,visi)

    return max(ans)



A = [1]
B= [2]
N = 3
H = [0,1,2]
print(solution(N,A,B,H))