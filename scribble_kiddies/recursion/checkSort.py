def Sorted(A,i,n):
    if i == n-1:
        return True
    if A[i] > A[i+1]:
        return False
    if Sorted(A,i+1,n):
        return True
    else:
        return False
print(Sorted([1,2,4,3],0,4))