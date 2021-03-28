class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(n):
            if i != n-1 and a[i] == a[i+1]:
                continue
            if A[i] == n-1-i:
                return 1
        return -1

A = Solution()

arr = [0]
a = A.solve(arr)
print(a)