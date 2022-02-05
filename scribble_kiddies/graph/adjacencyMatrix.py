## Create Matrix
def createMatrix(n):
    M  = []
    for i in range(n):
        M.append([])
        for j in range(n):
            M[i].append(0)
    return M

## Print Matrix
def printMatrix(A,n):
    for i in range(n):
        for j in range(n):
            print(A[i][j],end = " ")
        print()

## Undirected graph Adjacency matrix
def uAdjacencyMatrix(nodes,edges):
    MATRIX = createMatrix(nodes)
    for i in range(edges):
        node1,node2 = input().split()
        MATRIX[int(node1)][int(node2)] = 1
        MATRIX[int(node2)][int(node1)] = 1
    return MATRIX

printMatrix(uAdjacencyMatrix(7,7),7)






