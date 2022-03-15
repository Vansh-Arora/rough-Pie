def mergeNcount(arr,l,m,r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = 0
    j = 0
    k = l
    n1 = len(left)
    n2 = len(right)
    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            k += 1
            res += (n1 - i)
            j += 1
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
    return res
def divide(arr,l,r):
    res = 0
    if l < r:
        m = (l+r) // 2
        res += divide(arr,l,m)
        res += divide(arr,m+1,r)
        res += mergeNcount(arr,l,m,r)
    return res

