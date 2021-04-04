class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        j = 1
        n = len(A)
        i = 0
        while i < j and j<n:
            print("A[{}] = {} A[{}] = {}".format(i,A[i],j,A[j]))
            if A[j] - A[i] == B:
                return 1
            elif A[j] - A[i] < B:
                j += 1
            elif A[j] - A[i] > B:
                i += 1
                if i == j:
                    j += 1
        return 0

A = Solution()
a = A.diffPossible([ 2, 14, 18, 23, 25, 36, 40, 44, 44, 53, 55, 68, 71, 80, 94 ],1)
print(a)