def sort(A):
    n = len(A)
    for curr in range(n-1):  # place all elements at their respective places
        item = A[curr]         # taking each element iteratively
        pos = curr             # cycle sort ensures that previous elemnts are sorted so we check no. of elements
                               # smaller after given place and shift the element by those number of places
        for i in range(curr+1,n):
            if A[i] < item:
                pos += 1
        item,A[pos] = A[pos],item   # Now the item becomes the elemnt which has been taken out from the array
        while curr != pos:          # We repeat the above cycle till the element at curr position is found
            pos = curr
            for i in range(curr+1,n):
                if A[i] < item:
                    pos += 1
            item,A[pos] = A[pos],item


if  __name__ == "__main__":
    A =   [123,45,67,8,9,0,65,4,33,657,9]
    sort(A)
    print(A)