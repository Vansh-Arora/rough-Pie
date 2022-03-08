## Select the minimum element and place it at cur position
def sort(A):
    n = len(A)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if A[j] < A[min]:
                min = j
        A[i],A[min] = A[min],A[i]


if __name__ == "__main__":
    A = [2,1,4,7,5]
    sort(A)
    print(A)