def lomuto(A,l,r):
    ind = l
    pivot = A[r][1]
    for i in range(l,r):
        if A[i][1] < pivot:
            A[ind],A[i] = A[i],A[ind]
            ind += 1
    A[ind],A[r] = A[r],A[ind]
    return ind
def qSort(A,l,r):
    if l < r:
        p = lomuto(A,l,r)
        qSort(A,l,p-1)
        qSort(A,p+1,r)

def selector(A):
    qSort(A,0,len(A)-1)
    n = len(A)
    ans = []
    ans.append(A[0])
    for i in range(1,n):
        if A[i][0] >= ans[-1][1]:
            ans.append(A[i])    
    return ans

if __name__ == "__main__":
    A = [[0,1],[1,3],[2,5],[1,2]]
    ans = selector(A)
    print(ans)
