def getSub(A,k):
    sub = {}
    sum = 0
    for i in A:
        sum += i
        if sum == k:
            return True
        if k-i in sub:
            return True
        sub[sum] = 0
    return False


if __name__ == "__main__":
    ans = getSub([13,3,-1],13)
    print(ans)

