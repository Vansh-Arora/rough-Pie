def maxSubArray(A):
    maxi = float("-inf")
    sumYet = 0
    for i in A:
        sumYet += i
        maxi = max(maxi,sumYet)
        sumYet = max(sumYet,0) # if someYet goes below 0, update sumYet to 0
    return maxi

if __name__ == "__main__":
    A = [-100,-200,-300,-200,-400,-1800,-1500]
    print(maxSubArray(A))