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



if __name__ == "__main__":
    A = [1,2,6,78,90]
    print(binarySearch(A,6))