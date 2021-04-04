class Solution:
    def removeDuplicates(self,A):
        if len(A) == 1:
            return 1
        else:
            n = len(A)
            i = 1
            j = 0
            while i < n:
                if A[i] != A[j]:
                    j += 1
                    A[j] = A[i]
                i += 1
            A = A[:j+1]
            return len(A)

A = Solution()
a = A.removeDuplicates([5000,5000,5000])
print(a)