class Solution:
    def removeDuplicates(self,A):
        if len(A) < 3:
            return len(A)
        else:
            n = len(A)
            i = 1
            j = 0
            count = 1
            while i < n:
                if A[i] != A[j]:
                    j += 1
                    A[j] = A[i]
                    count = 1
                elif count < 2:
                    j += 1
                    A[j] = A[i]
                    count += 1
                i += 1
            A = A[:j+1]
            return len(A)

A = Solution()
a = A.removeDuplicates([5000,5000,5000])
print(a)