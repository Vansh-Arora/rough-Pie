class Solution:
    def solve(self, A):
        n = len(A)
        ans = A.split()
        B = ''
        for i in reversed(ans):
            B += i + " "
        return (B.rstrip())

A = Solution()
A.solve('hello vansh')
