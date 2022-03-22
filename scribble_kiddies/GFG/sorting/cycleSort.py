def sort(A):
    n = len(A)
    for curr in range(n):
        item = A[curr]
        pos = curr
        for i in range(curr+1,n):
            if A[i] < item:
                pos += 1
        item,A[pos] = A[pos],item
        while curr != pos:
            pos = curr
            for i in range(curr+1,n):
                if A[i] < item:
                    pos += 1
            item,A[pos] = A[pos],item

