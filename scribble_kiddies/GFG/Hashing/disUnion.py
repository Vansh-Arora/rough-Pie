def getDis(A,B):
    inter = {}
    for i in A:
        if i not in inter:
            inter[i] = 0
    for i in B:
        if i not in inter:
            inter[i] = 1
    for i in inter:
            print(i)

if __name__ == "__main__":
    getDis([1,2,4,5,6,7,8,1,2,3,4,5,6,7,8],[1,1,2,2,3,100,200,300,56])