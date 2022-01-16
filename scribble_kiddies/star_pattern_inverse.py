def Pattern2(n,i):
    if(n<1):
        return
    if(i==0):
        Pattern2(n-1,0)
    if(i<n):
        print('*',end='')
        Pattern2(n,i+1)
    else:
        print()
Pattern2(5,0)