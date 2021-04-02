class Solution:
    def merge(self, A, B):
        m = len(A)
        n = len(B)
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
        i = 0
        while i < m:
            A[i] = C[i]
            i += 1
        while i < m+n:
            A.append(C[i])
            i += 1
        return A
A = Solution()
a = A.merge([1,3],[2,5,6])
print(a)
            