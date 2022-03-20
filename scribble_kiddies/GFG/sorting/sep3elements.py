def seperate(A):
    zero = 0
    one = 0
    two = len(A)-1
    while one<=two:
        if A[one] == 0:
            A[zero],A[one] = A[one],A[zero]
            one += 1
            zero += 1
        elif A[one] == 1:
            one += 1
        else:
            A[one],A[two] = A[two],A[one]
            two -= 1

if __name__ == "__main__":
    A = [0,2,1,0,1,0,0,0,1,1,1,2,1,2,2,0,0]
    seperate(A)
    print(A)