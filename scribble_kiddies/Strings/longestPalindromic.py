def longestPalindrome(self,A):
    def check(A,l,r):
        while l >= 0 and r < len(A) and A[l] == A[r]:
            l -= 1
            r += 1

        return r-l - 1
    st = 0
    en = 0
    for i in range(len(A)):
        l1 = check(A,i,i)
        l2 = check(A,i,i+1)
        l = max(l1,l2)
        if l > (en - st)+1:
            st = i - ((l-1)//2)
            en = i + (l//2)
    return A[st:en+1]

print(longestPalindrome("abb"))