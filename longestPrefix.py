class Solution:
    def getCommon(self,A,B):
        i = 0
        while i < (min(len(A),len(B))):
            if A[i] == B[i]:
                i += 1
            else:
                break
        return(A[:i])

    def longestCommonPrefix(self, A):
        if len(A) == 0:
            return None
        prefix = A[0]
        for i in A:
            prefix = self.getCommon(prefix,i)
        return prefix

a = Solution()
print(a.longestCommonPrefix(['ab','AB']))



