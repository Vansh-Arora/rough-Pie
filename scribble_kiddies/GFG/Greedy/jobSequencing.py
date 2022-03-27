def lomuto(A,B,l,r):
    ind = l
    pivot = A[r]
    for i in range(l,r):
        if A[i] > pivot:
            A[ind],A[i] = A[i],A[ind]
            B[ind],B[i] = B[i],B[ind]
            ind += 1
    A[ind],A[r] = A[r],A[ind]
    B[ind],B[r] = B[r],B[ind]
    return ind
def qSort(A,B,l,r):
    if l < r:
        p = lomuto(A,B,l,r)
        qSort(A,B,l,p-1)
        qSort(A,B,p+1,r)
def seq(DL,P):
    qSort(P,DL,0,len(DL)-1)
    print(P)
    print(DL)
    profit = 0
    n = len(P)
    dl = [-1 for i in range(n)]
    print(dl)
    for i in range(n):
        temp = DL[i]
        while temp > 0 and dl[temp-1] != -1:
            temp -= 1
        if temp != 0 and dl[temp-1] == -1:
            dl[temp-1] = i
            profit += P[i]
        print(dl)
            
    return profit


if __name__ == "__main__":
    DL = [2,1,2,1,3]
    P = [100,50,10,20,30]
    #DL = [2,2,3,3]
    #P = [50,60,20,30]
    ans = seq(DL,P)
    print(ans)