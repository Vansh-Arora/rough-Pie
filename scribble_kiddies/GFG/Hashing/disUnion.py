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
