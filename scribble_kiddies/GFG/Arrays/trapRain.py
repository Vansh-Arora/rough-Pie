def trap(A):
    n = len(A)
    lmax = [-1 for i in range(n)]
    rmax = [-1 for i in range(n)]
    lmax[0] = A[0]
    for i in range(1,n):
        lmax[i] = max(lmax[i-1],A[i])
    rmax[n-1] = A[n-1]
    for i in range(n-2,-1,-1):
        rmax[i] = max(rmax[i+1],A[i])
    ans = 0
    for i in range(n):
        ans += (min(lmax[i],rmax[i]) - A[i])
    
    return ans

if __name__ == "__main__":
    A = [5,0,6,2,3]
    ans = trap(A)
    print(ans)