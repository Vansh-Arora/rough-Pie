# Recursive Solution
''''
def lcs(s1,s2,m,n):
    if m == 0 or n == 0:
        return 0
    if s1[m-1] == s2[n-1]:
        return 1 + lcs(s1,s2,m-1,n-1)
    else:
        return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
'''
## Using DP
m = 4
n = 3
S = [[-1 for i in range(n+1)] for j in range(m+1)]
def lcs(s1,s2,m,n):
    if S[m][n] != -1:
        return S[m][n]
    if m == 0 or n == 0:
        S[m][n] = 0
    elif s1[m-1] == s2[n-1]:
        S[m][n] = 1 + lcs(s1,s2,m-1,n-1)
    else:
        S[m][n] =  max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
    return S[m][n]

s1 = "BACD"
s2 = "BCD"
print(lcs(s1,s2,m,n))
