def lomuto(A,l,r):
    p = r
    j = l-1
    for i in range(r-1):
        if A[i] <= A[p]:
            j += 1
            A[i],A[j] = A[j],A[i]
    A[j+1],A[p] = A[p],A[j+1]
    print(A)