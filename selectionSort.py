def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if A[j] < A[min]:
                min = j
        A[min],A[i] = A[i],A[min]


arr = input().split()
arr = [int(i) for i in arr]
selectionSort(arr)
print(arr)