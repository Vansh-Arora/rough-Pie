def union(A,B):
    m = len(A)
    n = len(B)
    i = 0
    j = 0
    while i < m and j < n:
        if i != 0 and A[i] == A[i-1]:
            i += 1
            continue
        if j != 0 and A[j] == A[j-1]:
            j += 1
            continue