def fisrtLast(A,C,first,last):
    if first>=last:
        return [first,last]
    if A[first] == C and A[last] == C:
        return [first,last]
    if A[first] == C:
        return fisrtLast(A,C,first,last-1)
    elif A[last] == C:
        return fisrtLast(A,C,first+1,last)
    else:
        return fisrtLast(A,C,first+1,last-1)
print(fisrtLast("ABCAE","A",0,4))