def reverse(A,beg,end):
    while beg < end:
        A[beg],A[end] = A[end],A[beg]
        beg += 1
        end -= 1

if __name__ == "__main__":
    A = [1,2,3,4,5,6]
    reverse(A,0,5)
    print(A)