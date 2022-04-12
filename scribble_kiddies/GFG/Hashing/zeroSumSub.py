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
        