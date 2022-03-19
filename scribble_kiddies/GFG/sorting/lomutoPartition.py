# Lomuto partition ensures that pivot is placed at its right position
# It places all the elements smaller than or equal to pivot on left of pivot
# all elemnts greater than or equal to pivot on right of pivot.
def lomuto(A,l,r):
    p = r
    j = l-1
    for i in range(r):
        if A[i] < A[p]:
            j += 1
            A[i],A[j] = A[j],A[i]
    A[j+1],A[p] = A[p],A[j+1]
    print(A)
if __name__ == "__main__":
    lomuto([2,3,4,13,1,3,6,5,4],0,8)