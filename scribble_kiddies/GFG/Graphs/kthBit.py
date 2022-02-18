def kBit(n,k):
    if (n & (1 << k-1)):
        print(True)
    else:
        print("False")

kBit(13,2)