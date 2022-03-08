def sort():
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if A[j] < A[min]:
                min = j
        A[i],A[min] = A[min],A[i]
