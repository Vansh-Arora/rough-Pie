def lomuto(A,l,r):
    ind = l
    pivot = A[r][0]
    for i in range(l,r):
        if A[i][0] < pivot:
            A[ind],A[i] = A[i],A[ind]
            ind += 1
    A[ind],A[r] = A[r],A[ind]
    return ind
def qSort(A,l,r):
    if l < r:
        p = lomuto(A,l,r)
        qSort(A,l,p-1)
        qSort(A,p+1,r)
def merge(A):
    n = len(A)
    qSort(A,0,n-1)
    res = 0
    for i in range(1,n):
        if A[i][0] < A[res][1]:
            A[res][0] = min(A[res][0],A[i][0])
            A[res][1] = max(A[res][1],A[i][1])
        else:
            res += 1
            A[res] = A[i]
    for i in range(res+1):
        print(A[i])

arr = [[2,4],[1,3],[8,10],[5,7],[6,9]]
merge(arr)
