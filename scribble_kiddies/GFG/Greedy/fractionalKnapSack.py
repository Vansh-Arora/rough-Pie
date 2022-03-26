def lomuto(A,B,l,r):
    ind = l
    pivot = B[r]/A[r]
    for i in range(l,r):
        if B[i]/A[i] < pivot:
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
def knap(Weight,Value,Capacity):
    qSort(Weight,Value,0,len(Value)-1)
    i = len(Value) - 1
    ans = 0
    while Capacity > 0 and i >= 0:
        if Weight[i] > Capacity:
            ans += Capacity * (Value[i]/Weight[i])
            Capacity = 0
        else:
            Capacity -= Weight[i]
            ans += Value[i]
        i -= 1
    return ans

if __name__ == "__main__":

    A = [50,20,30]
    B = [600,500,400]
    ans = knap(A,B,70)
    print(ans)
