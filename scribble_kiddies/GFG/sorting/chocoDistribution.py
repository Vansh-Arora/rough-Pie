def distribute(A,m):
    n = len(A)
    if m > n:
        return -1
    A.sort()
    mini = float("inf")
    for i in range(n-m+1):
        temp = A[i+m-1] - A[i]
        if temp < mini:
            mini =  temp
    return mini

if __name__ == "__main__":
    A = [7,3,2,4,9,12,56]
    A = [3,4,1,9,56,7,9,12]
    ans = distribute(A,3)
    print(ans)

    
