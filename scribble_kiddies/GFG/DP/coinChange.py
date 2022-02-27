ways = 0 
def coin(sum, cur, A,ans):
    global ways
    if cur == sum:
        ways += 1
        print(ans)
        return ways
    if cur > sum:
        return ways
    for i in A:
        coin(sum,cur+i,A,ans+str(i))
    return ways

print(coin(4,0,[1,2,3],''))