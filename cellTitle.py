class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans = ''
        while(A>26):
            r = A % 26
            if r == 0:
                r = 26
                A -= 1
            r = chr(r+64)
            ans = r + ans
            A = A//26
        ans = chr(A+64) + ans
        return ans

A = Solution()
a = A.convertToTitle(52)
print(a)