def Sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if(A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]

S = [6,2,5,10,1]
Sort(S)
print(S)