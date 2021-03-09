class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        ans = 0
        toPlaceValue = len(A)-1
        for i in A:
            ans += (ord(i) - 64) * (26 ** toPlaceValue)
            toPlaceValue -= 1
        return ans
A = Solution()
a = A.titleToNumber('UI')
print(a)