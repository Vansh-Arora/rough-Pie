def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                A[j+1],A[j] = A[j],A[j+1]

arr = input().split()
arr = [int(i) for i in arr]
bubbleSort(arr)
print(arr)