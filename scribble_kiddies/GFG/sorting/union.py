def union(A,B):
    m = len(A)
    n = len(B)
    i = 0
    j = 0
    while i < m and j < n:
        if i != 0 and A[i] == A[i-1]:
            i += 1
            continue
        if j != 0 and B[j] == B[j-1]:
            j += 1
            continue
        if A[i] < B[j]:
            print(A[i],end = " ")
            i += 1
        elif B[j] <  A[i]:
            print(B[j],end = " ")
            j += 1
        else:
            print(A[i],end = " ")
            i += 1
            j += 1
    while i < m:
        if i != 0 and A[i] == A[i-1]:
            i += 1
            continue
    while j < n:
        if j != 0 and B[j] == B[j-1]:
            j += 1
            continue



            
if __name__ == "__main__":
    A = [1,1,3,5,6,7,8,9]
    B = [6,6,7,8]
    union(A,B)
