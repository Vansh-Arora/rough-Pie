def frequency(A):
    freq = {}
    for i in A:
        if i in freq:
            A[i] += 1
        else:
            A[i] = 1
    print(A)