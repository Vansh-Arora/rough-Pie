def merge(arr, l, m, r):
    lA = arr[l:m+1]
    rA = arr[m+1:r+1]
    print(lA,rA)
    L = 0
    R = 0
    i = 0
    n1 = len(lA)
    n2 = len(rA)
    while L < n1 and R < n2:
        if lA[L] < rA[R]:
            arr[i] = lA[L]
            L += 1
        else:
            arr[i] = rA[R]
            R += 1
        i += 1
    while L < n1:
        arr[i] = lA[L]
        i += 1
        L += 1
    while R < n2:
        arr[i] = rA[R]
        i += 1
        R += 1

    print(arr)
        
    # code here
def mergeSort(arr, l, r):
    #code here
    if r > l:
        m = (l +r)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)

A = [5,3,2]
mergeSort(A,0,2)
print(A)