def srch(A,B,l,r):
    ans = -1
    while l <= r:
        m = (l+r)//2
        if A[m] < B:
            ans = m
            r = m-1
        else:
            l = m + 1
    return ans

def bs(A,B,l,r):
    if l <= r:
        m = (l + r)//2
        if A[m] == B:
            return m
        elif A[m] < B:
            return bs(A,B,m+1,r)
        else:
            return bs(A,B,l,m-1)
    return -1

def search(A, B):
    p = srch(A,A[0],0,len(A)-1)
    if p == -1:
        return bs(A,B,0,len(A)-1)
    if B < A[0]:
        return bs(A,B,p,len(A)-1)
    else:
        return bs(A,B,0,p-1)

A = [ 1, 7, 67, 133, 178 ]
B = 1
search(A,B)