class Solution:
    def reverse(self, A):
        if A == 0:
            return 0
        else:
            binA = []
            len = 1
            while A != 1:
                binA.append(A%2)
                len += 1
                A = A//2
            binA.append(1)
            B = 31
            ans = 0
            for i in binA:
                ans = ans + i*(2**B)
            return ans

A = Solution()
A.reverse(11)

