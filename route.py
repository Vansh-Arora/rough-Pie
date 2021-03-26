import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        mn = A+B-2
        m = A-1
        n = B-1
        return math.factorial(mn)//(math.factorial(m) * math.factorial(n))
