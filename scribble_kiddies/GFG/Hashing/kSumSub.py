def getSub(A,k):
    sum = A[0]
    start = 0
    for i in range(1,len(A)):
        if sum == k:
            return True
        elif sum > K:
            sum -= A[start]
            start += 1
        sum += A[i]
    return False

