def comp(A,B):
    A = str(A)
    B = str(B)
    n = len(A)
    m = len(B)
    i = 0
    j = 0
    while i < n and j < m:
        if A[i] < B[j]:
            return B
        if B[j] < A[i]:
            return A
        i += 1
        j += 1
    while i < n:
        if A[i] < B[m-1]:
            return B
    while j < m:
        if B[j] < A[n-1]:
            return A
A = [1,2,3,30,31,13,1330,9]
A = [str(i) for i in A]
print(comp(30,3))