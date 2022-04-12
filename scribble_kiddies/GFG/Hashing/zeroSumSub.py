def getSub(A):
    sub = {}
    sum = 0
    for i in A:
        sum += i
        if sum in sub:
            return True
        else:
            sub[sum] = 0
    return False

if __name__ == "__main__":
    ans = getSub([1,2,4,5,6,7,8,1,2,3,4,5,6,7,8,-9,-8,0])
    print(ans)
        