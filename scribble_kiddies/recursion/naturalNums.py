def natural(n):
    if(n==0):
        return   
    natural(n-1)
    print(n)
natural(9)