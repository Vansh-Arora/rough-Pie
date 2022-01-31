count = 0

def isSafe(G,I,J,n):

    ## Checking the rows above in same column
    for i in range(I+1):
        if G[i][J]:
            return False
    
    ## checking the left diagonal
    i = I
    j = J
    while i >= 0 and j >= 0:
        if G[i][j]:
            return False
        i -= 1
        j -= 1
    
    ## Checking the right diagonal
    i = I
    j = J
    while i >= 0 and j < n:
        if G[i][j]:
            return False
        i -= 1
        j += 1
    return True


def createGrid(n):
    G = []
    for i in range(n):
        G.append([])
        for j in range(n):
            G[i].append(0)
    return G

def helper(G,n,row):
    global count
    if row == n:
        print(G)
        count += 1
        return
    for j in range(n):
        if isSafe(G,row,j,n):
            G[row][j] = 1
            helper(G,n,row+1)
            G[row][j] = 0
    
def nQueen(n):
    G = createGrid(n)
    helper(G,n,0)

nQueen(4)
print(count)