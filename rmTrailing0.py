class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0
        while(A>=5):
            count += A//5
            A = A//5
        return count