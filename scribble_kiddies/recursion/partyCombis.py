def Party(P):
    if(P==0):
        return 1
    if(P==1):
        return 1
    return Party(P-1)+((P-1)*Party(P-2))
print(Party(3))