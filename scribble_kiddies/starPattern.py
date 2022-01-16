def Pattern1(n,i):
    if(n==0):
        return
    if i<n:
        print('*',end="")
        Pattern1(n,i+1)
    else:
        print()
        Pattern1(n-1,0)
Pattern1(5,0)