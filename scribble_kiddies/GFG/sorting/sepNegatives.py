def seperate(A,l,r):
    i = l-1
    j = r+1
    while True:
        i += 1
        while A[i] < 0:
            i += 1
        j -= 1
        while A[j] >= 0:
            j -= 1
        if i >= j:
            return
        A[i],A[j] = A[j],A[i]

if __name__ == "__main__":
    A = [5,3,12,8,5,-10,19,-1,-99,-910]
    seperate(A,0,9)
    print(A)