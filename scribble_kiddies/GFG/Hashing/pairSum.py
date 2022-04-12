def getPair(A,S):
    table = {}
    for i in A:
        if S - i in table:
            return True
        else:
            if i not in table:
                table[i] = 0
    return False

if __name__ == "__main__":
    ans = getPair([1,2,4,5,6,7,8,1,2,3,4,5,6,7,8],17)
    print(ans)