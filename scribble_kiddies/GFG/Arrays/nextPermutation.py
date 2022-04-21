def nextPermutation(n, arr):
    flag= 1
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            ind = i+1
            flag = 0
            break
    if flag:
        arr.reverse()
        return arr
    ind2 = ind
    for i in range(n-1,ind,-1):
        if (arr[ind-1] < arr[i]) and (arr[i] < arr[ind]):
            if (arr[i]<arr[ind2]):
                ind2 = i

    arr[ind-1],arr[ind2] = arr[ind2],arr[ind-1]
    while ind < n-1:
        arr[ind],arr[n-1] = arr[n-1],arr[ind]
        ind += 1
        n -= 1
    return arr