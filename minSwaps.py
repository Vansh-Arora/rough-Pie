def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    i = 0
    while i < n:
        if arr[i] == i+1:
            i += 1
        else:
            ind = i
            ind2 = arr[i]-1
            arr[ind],arr[ind2] = arr[ind2],arr[ind]
            swaps += 1
    return swaps
print(minimumSwaps([4,3,1,2]))
