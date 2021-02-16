def getScore(A, B):
    inter = A.intersection(B)
    uniqueA = A - B
    uniqueB = B - A
    return min(inter, uniqueA, uniqueB)