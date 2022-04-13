def getSub(A,k):
    sub = {}
    sum = 0
    for i in A:
        sum += i
        if sum == k:
            return True
        if sum-k in sub:
            return True
        sub[sum] = 0
    return False


if __name__ == "__main__":
    ans = getSub([1,3,-1,11,2],13)
    print(ans)

