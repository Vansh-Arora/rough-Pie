class Node:
    def __init__(self,data,ind):
        self.data = data
        self.ind = ind


def maximumGap(A):
    n = len(A)
    B = [Node(A[i],i) for i in range(n)]
    B.sort(key = lambda i : i.data)
    maxInd = [-1 for i in range(n)]
    maxInd[-1] = B[-1].ind
    for i in range(n-2,-1,-1):
        maxInd[i] = max(B[i].ind,maxInd[i+1])
    ans = float("-inf")
    for i in range(n):
        ans = max(maxInd[i] - B[i].ind,ans)
    return ans


A = [3, 5, 4, 2]
print(maximumGap(A))
