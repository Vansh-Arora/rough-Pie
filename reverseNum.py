class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        B = str(abs(A))
        C = ''
        for i in range(len(B)-1,-1,-1):
            C += B[i]
        C = int(C)
        if A < 0:
            C = -C
        if C < -2147483648 or C > 2147483647:
            return 0
        return (C)

a = Solution()
print(a.reverse(214))