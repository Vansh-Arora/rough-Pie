def getMaxSum(A):
    sumYet = 0
    maxi = float("-inf")
    for i in A:
        sumYet += i
        maxi = max(sumYet,maxi)
        sumYet = max(sumYet,0)
    return maxi

def getMinSum(A):
    sumYet = 0
    mini = float("inf")
    for i in A:
        sumYet += i
        mini = min(sumYet,mini)
        sumYet = min(0,sumYet)
    return mini

def circularSum(A):
    s = 0
    for i in A:
        s += i
    return max(getMaxSum(A),s-getMinSum(A))

A = [8,-4,3,-5,4]
ans = circularSum(A)
print(ans)