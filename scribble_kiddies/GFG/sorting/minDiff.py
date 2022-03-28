def getMinDiff(A):
    n = len(A)
    A.sort()
    mini = float("inf")
    for i in range(1,n):
        mini = min(mini,A[i]-A[i-1])
    return mini
    

if __name__ == "__main__":
    A = [23,56,87,99,97.6,98,76]
    print(getMinDiff(A))