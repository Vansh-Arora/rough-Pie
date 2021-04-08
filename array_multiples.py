def reduce(A):
    if len(A) == 2:
        return A
    n = len(A)
    if n % 2 != 0:
        last = n-1 
    else:
        last = n
    temp = []
    for i in range(0,last,2):
        temp.append(A[i]*A[i+1])
    if last < n:
        temp.append(A[last])
    return reduce(temp)
print(reduce([1,2,3,4,5]))