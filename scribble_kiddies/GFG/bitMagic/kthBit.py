# Method 1 (Left Shift)
def kBit(n,k):
    if (n & (1 << k-1)):
        print(True)
    else:
        print(False)

# Method 2 (Right Shift)
def kBitR(n,k):
    if ((n >> k-1) & 1):
        pritn(True)
    else:
        print(False)
kBit(13,2)
kBit(13,3)