def getPair(A,S):
    table = {}
    for i in A:
        if S - i in table:
            return True
        else:
            if i not in table:
                table[i] = 0
        
        