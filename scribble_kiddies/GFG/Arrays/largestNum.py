def comp(A,B):
    A = str(A)
    B = str(B)
    n = len(A)
    m = len(B)
    i = 0
    j = 0
    while i < n and j < m:
        if A[i] < B[j]:
            return 1
        if B[j] < A[i]:
            return 0
        i += 1
        j += 1
    while i < n:
        if A[i] < B[m-1]:
            return 1
    while j < m:
        if B[j] < A[n-1]:
            return 0
            
def part(A,l,r):
    p = A[r]
    ind = l
    for i in range(l,r):
        if A[i] < p:
            A[ind],A[i] = A[i],A[ind]
            ind += 1
    A[ind],A[r] = A[r],A[ind]
    return ind
def qSort(A,l,r):
    if l > r:
        return
    pivot = part(A,l,r)
    qSort(A,l,pivot-1)
    qSort(A,pivot+1,r)

A = [2,5,6,1,3,4]
qSort(A,0,5)
print(A)
    


A = [1,2,3,30,31,13,1330,9]
A = [str(i) for i in A]
#print(comp(30,3))