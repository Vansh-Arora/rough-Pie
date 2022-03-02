def Sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j > -1 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

S = [6,2,5,10,1]
Sort(S)
print(S)

