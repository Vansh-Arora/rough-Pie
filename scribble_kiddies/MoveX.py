def move(S,i,n,ans):
    if n <= 1:
        return S
    if i >= n:
        return ans + ("X"*(n-len(ans)))
    if S[i] != "X":
        ans += S[i]
        return move(S,i+1,n,ans)
    else:
        return move(S,i+1,n,ans)
A = "ABCFGXXBJGCXHJKHX"
print(move(A,0,len(A),""))
