def lomuto(A,l,r):
    p = r
    j = l-1
    for i in range(l,r):
        if A[i] < A[p]:
            j += 1
            A[i],A[j] = A[j],A[i]
    A[j+1],A[p] = A[p],A[j+1]
    return j+1

def find(A,k):
    r = len(A) - 1
    l = 0
    while l <= r:
        ind = lomuto(A,l,r)
        if ind == k-1:
            return A[ind]
        if ind < k-1:
            l = ind+1
        else:
            r = ind-1
    return -1

if __name__ == "__main__":
    A = [8,4,7,9,3,10,5]
    A = [1]
    ans = find(A,1)
    print(ans)