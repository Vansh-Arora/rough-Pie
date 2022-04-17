class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        dup = {}
        for i in A:
            if i in dup:
                return i
            else:
                dup[i] = 0
        return -1
