class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        ans = [[] for i in range((2*n)-1)]
        for i in range(n):
            for j in range(n):
                ans[i+j].append(A[i][j])
        return ans