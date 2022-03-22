def sort(A):
    n = len(A)
    for curr in range(n-1):
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


if  __name__ == "__main__":
    A =   [123,45,67,8,9,0,65,4,33,657,9]
    sort(A)
    print(A)