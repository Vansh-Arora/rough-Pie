def create(n):
    for i in range(n):
        for j in range(2*n):
            if j <= i or j >= (2*n)-(i+1):
                print("*",end="")
            else:
                print(" ",end = "")
        print()
    for i in range(n):
        for j in range(2*n):
            if j < n-i or j >=(n+i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
            

            

create(5)