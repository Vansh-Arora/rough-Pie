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
            print(A)
            return j
        A[i],A[j] = A[j],A[i]

        
hoare([5,3,8,4,2,7,1,10],0,7)