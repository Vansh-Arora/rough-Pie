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
            ANS.append(A[i])
    print(ANS)
    return index

if __name__ == "__main__":
    A = [5,3,12,8,5]
    pivot = part(A,0,4,0)
    print(pivot)