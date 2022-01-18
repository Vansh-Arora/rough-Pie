def rev(str,n):
    if n==0:
        print(str[n])
        return
    print(str[n])
    rev(str,n-1)
rev("BAC",2)
        