def meet(A,B):
    n = len(A)
    A.sort()
    B.sort()
    maxi = float("-inf")
    guests = 0
    i = 0
    j = 0
    while i < n:
        if A[i] < B[j]:
            guests += 1
            i += 1
        elif B[j] < A[i]:
            guests -= 1
            j += 1
        else:
            i += 1
            j += 1
        if guests > maxi:
            maxi = guests
    return maxi

if __name__ == "__main__":
    A=[900,940,950,1100,1500,1800]
    B=[910,1200,1120,1130,1900,2000]
    print(meet(A,B))
