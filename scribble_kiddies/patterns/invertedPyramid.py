def create(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j <= (n-i):
                print(" ",end = "")
            else:
                print("*",end = "")
        print()
def createInverterd(n):
    for i in range(n):
        for j in range(n-i):
            print(n,end="")
        print()

create(5)