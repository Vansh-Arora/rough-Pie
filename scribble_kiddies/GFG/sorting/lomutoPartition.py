# Lomuto partition ensures that pivot is placed at its right position
# It places all the elements smaller than or equal to pivot on left of pivot
# all elemnts greater than or equal to pivot on right of pivot.
def lomuto(A,l,r):
    p = r
    j = l-1
    for i in range(l,r):
        if A[i] < A[p]:
            j += 1
            A[i],A[j] = A[j],A[i]
    A[j+1],A[p] = A[p],A[j+1]
    return j+1

def qSort(A,l,r):
    if l < r:
        p = lomuto(A,l,r)
        qSort(A,l,p-1)
        qSort(A,p+1,r)

if __name__ == "__main__":
    A = [8,4,7,9,3,10,5]
    qSort(A,0,6)
    print(A)