## return 1 if A is smaller than B
def smaller(A,B):
    A = str(A)
    B = str(B)
    a = A + B
    b = B + A
    if a > b:
        return 0
    else:
        return 1

def part(A,l,r):
    p = A[r]
    ind = l
    for i in range(l,r):
        if not smaller(A[i],p):
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
def part(A,l,r):
    p = A[r]
    ind = l
    for i in range(l,r):
        if not smaller(A[i],p):
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

def largestNumber(self, A):
    B = [i for i in A]
    qSort(B,0,len(A)-1)
    if B[0] == 0:
        return '0'
    B = [str(i) for i in B]
    return "".join(B)