def hoare(A,l,r):
    p = A[l]
    i = l-1
    j = r+1
    while True:
        i += 1
        while A[i] < p:
            i += 1
        j -= 1
        while A[j] > p:
            j -= 1
        if i >= j:
            return j
        A[i],A[j] = A[j],A[i]

def qSort(A,l,r):
    if l < r:
        p = hoare(A,l,r)
        qSort(A,l,p)
        qSort(A,p+1,r)

if __name__ == "__main__": 
    A = [5,3,8,4,2,7,1,10]
    qSort(A,0,7)
    print(A)