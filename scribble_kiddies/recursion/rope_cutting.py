def cut(n,A,B,C,S,P,ans):
    if S>n:
        return ans
    if S==n:
        ans.append(P)
        return ans
    cut(n,A,B,C,S+A,P+1,ans)
    cut(n,A,B,C,S+B,P+1,ans)
    cut(n,A,B,C,S+C,P+1,ans)
    return max(ans)
print(cut(5,4,2,6,0,0,[-1]))
