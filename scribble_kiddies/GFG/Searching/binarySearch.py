# Iterative approach
def binarySearch(A,n):
    s = len(A)
    start = 0
    end = s-1
    while start <= end:
        mid = (start + end)//2
        if A[mid] == n:
            return mid
        elif A[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# Recursive Approcah
def binSearch(A,k,start,end):
    if start > end:
        return -1
    mid = (start + end)//2
    if A[mid] == k:
        return mid
    if A[mid] > k:
        return binSearch(A,k,start,mid-1)
    else:
        return binSearch(A,k,mid+1,end)

if __name__ == "__main__":
    A = [1,2,6,78,90]
    a = [1,2,3,4,5]
    print(binarySearch(A,6))
    print(binSearch(a,4,0,4))