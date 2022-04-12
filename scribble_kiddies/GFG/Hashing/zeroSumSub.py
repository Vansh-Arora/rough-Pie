def getSub(A):
    sub = {}
    sum = 0
    for i in A:
        sum += i
        if sum == 0:
            return True
        if sum in sub:
            return True
        sub[sum] = 0
    return False

if __name__ == "__main__":
    ans = getSub([0,1,2])
    print(ans)
        