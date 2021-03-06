class Solution:
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if n == 0:
            C = A
        elif m == 0:
            C = B
        else:
            i = 0
            j = 0
            C = []
            while i < m and j < n:
                if A[i] < B[j]:
                    C.append(A[i])
                    i += 1
                else:
                    C.append(B[j])
                    j += 1
            while i < m:
                C.append(A[i])
                i += 1
            while j < n:
                C.append(B[j])
                j += 1
        
        nm = n + m
        if (nm)%2 == 0:
            median = (C[nm//2] + C[(nm//2) - 1])/2
        else:
            median = C[nm//2]
        return median
A = Solution()
a = A.findMedianSortedArrays([0,23],[22,111])
print(a)
            