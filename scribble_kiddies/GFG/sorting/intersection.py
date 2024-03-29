def intersection(A,B):
    i = 0
    j = 0
    m = len(A)
    n = len(B)
    while i < m and j < n:
        if i > 0 and A[i] == A[i-1]:
            i += 1
            continue
        if A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            print(A[i],end = " ")
            i += 1
            j += 1
            
if __name__ == "__main__":
    A = [1,1,3,5,6,7,8]
    B = [6,6,7,8]
    intersection(A,B)
