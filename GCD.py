class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if B>A:
            A,B = B,A
        if B == 0:
            return A
        if A%B == 0:
            return B
        else:
            return self.gcd(B,A%B)

a = Solution()
b = a.gcd(2016,2448)
print(b)