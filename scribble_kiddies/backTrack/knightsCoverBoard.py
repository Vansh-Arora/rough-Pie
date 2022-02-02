from traceback import print_tb


def isSafe(visi,I,J,N):
    if I<0 or J<0 or I >= N or J >= N or visi[I][J]:
        return False
    return True


def createGrid(n):
    G = []
    for i in range(n):
        G.append([])
        for j in range(n):
            G[i].append(0)
    return G

def helper(i,j,n,G,visited,count):
    if count == (n*n)-1:
        G[i][j]=count
        print(G)
        return
    if count >= n*n:
        return

    visited[i][j]=1
    G[i][j]=count
    I = [-1,-1,-2,2,1,1,-2,2]
    J = [2,-2,-1,-1,2,-2,1,1]
    for k in range(8):
        if isSafe(visited,i+I[k],j+J[k],n):
            helper(i+I[k],j+J[k],n,G,visited,count+1)
    visited[i][j] = 0
    G[i][j] = 0
    





def cover(n):
    G = createGrid(n)
    visited = createGrid(n)
    helper(0,0,n,G,visited,0)

cover(5)