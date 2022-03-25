def reverse(A,beg,end):
    while beg < end:
        A[beg],A[end] = A[end],A[beg]
        beg += 1
        end -= 1

def rotate(A,k):
    n = len(A)
    if k >= n:
        k %= n
    reverse(A,0,k-1)
    reverse(A,k,n-1)
    reverse(A,0,n-1)
    

if __name__ == "__main__":
    A = [1,2,3,4,5,6]
    rotate(A,2)
    print(A)