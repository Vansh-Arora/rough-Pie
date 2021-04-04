class Solution:
    def minVal(self,a,b,c):
        return max(abs(a-b), abs(b-c), abs(c-a))
    def minimize(self, A, B, C):
        i = 0
        j = 0
        k = 0
        mini = float("inf")
        while i < len(A) and j < len(B) and k < len(C):
            mini = min(mini,self.minVal(A[i],B[j],C[k]))
            if A[i] == min(A[i],B[j],C[k]):
                i += 1
            elif B[j] == min(A[i],B[j],C[k]):
                j += 1
            else:
                k += 1
            
        return mini

A = Solution()
print(A.minimize([1, 4, 10],[2, 15, 20],[10, 12]))