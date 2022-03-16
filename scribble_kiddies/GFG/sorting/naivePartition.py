def part(A,l,r,p):
    ANS = []
    index = l-1
    for i in range(l,r+1):
        if A[i] < A[p]:
            ANS.append(A[i])
            index += 1
    for i in range(l,r+1):
        if A[i] == A[p]:
            ANS.append(A[i])
            index += 1
    for i in range(l,r+1):
        if A[i] > A[p]:
            ANS.append(ANS.append(A[i]))
    print(ANS)
    return index