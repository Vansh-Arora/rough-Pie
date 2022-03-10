def intersection(A,B):
    i = 0
    j = 0
    m = len(A)
    n = len(B)
    while i < m and j < n:
        if i > 0 and A[i] == A[i-1]:
            continue
        if A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            print(A[i])
            i += 1
            j += 1

A = [1,3,5,6,7,8]
B = [6,6,7,8]
intersection(A,B)
