def maxi(A):
    res = 0
    n = len(A)
    if A[0]%2 == 0:
        odd = 0
    else:
        odd = 1
    count = 1
    for i in range(1,n):
        if A[i]%2 == 0:
            curr = 0
        else:
            curr = 1
        
        if curr ^ odd:
            count += 1
        else:
            count = 1
        odd = curr
        res = max(count,res)
    print(res)

maxi([1,1,1,1,12,25,10,3,7,9])
