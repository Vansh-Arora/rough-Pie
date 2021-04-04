def max1(A):
    i = 0
    j = 0
    start = -1
    end = -1
    n = len(A)
    while i<=j and j < n:
        if A[j] == 1 and j < n-1:
            j += 1
        elif A[j] == 1 and j == n-1:
            if (end - start)+1 < (j - i)+1:
                end = j
                start = i
            break
        elif A[j] != 1 and i != j:
            if (end - start)+1 < j - i:
                end = j-1
                start = i
            i = j
            if n - 1 - j < (end - start) + 1:
                break
        else:
            i += 1
            j += 1
    print("start = {} end = {}".format(start,end))
    print(A)
    print((end - start)+1)

max1([2,0,2,5,1,4,2,1,1,1,1,2,5,1,1,2,1,1,1,1,1])