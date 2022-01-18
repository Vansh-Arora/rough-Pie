def jump(A,n,i,asf):
    if i == n-1:
        print(asf)
        return
    if i >= n:
        return
    for j in range(1,7):
        jump(A,n,i+j,asf+str(j))

jump([1,2,3,4,5],5,0,"")