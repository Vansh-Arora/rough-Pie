# Merge Function
# Given an array with 2 individual sorted components
## first component: l-m     ## Second Component: (m+1)-r

def merge(arr, l, m, r):
    # Make 2 arrays from these components
    lA = arr[l:m+1]
    rA = arr[m+1:r+1]
    # Now merge 2 sorted arrays
    L = 0
    R = 0
    i = l # here i = l as each time main array will be sorted till l(starting point of present array)
    n1 = len(lA)
    n2 = len(rA)
    while L < n1 and R < n2:
        if lA[L] < rA[R]:
            arr[i] = lA[L]
            L += 1
        else:
            arr[i] = rA[R]
            R += 1
        i += 1
    while L < n1:
        arr[i] = lA[L]
        i += 1
        L += 1
    while R < n2:
        arr[i] = rA[R]
        i += 1
        R += 1

## Divide the array till it reaches to size 1
# then start merging
def mergeSort(arr, l, r):
    if r > l:
        m = (l +r)//2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge(arr,l,m,r)

if __name__ == "__main__":
    A = [5,3,2,80,1,25]
    mergeSort(A,0,5)
    print(A)