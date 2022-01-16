def power(a,b):
    if(b==0):
        return 1
    if(b==1):
        return a
    #return a*power(a,b-1)
    temp=power(a,b//2)
    if b%2 == 0:
        return temp*temp
    return a*temp*temp
print(power(2,5))