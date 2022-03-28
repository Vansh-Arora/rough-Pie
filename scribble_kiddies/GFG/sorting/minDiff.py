def getMinDiff(A):
    n = len(A)
    A.sort()
    mini = float("inf")
    for i in range(1,n):
        mini = min(mini,A[i]-A[i-1])
    return mini
        