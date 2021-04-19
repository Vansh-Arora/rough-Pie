def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    
arr = input().split()
arr = [int(i) for i in arr]
insertionSort(arr)
print(arr)