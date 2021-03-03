class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        n = len(A)
        LSV = [0]
        for i in range(1,n):
            j = i - 1
            while j > -1:
                if A[j] > A[i]:
                    LSV.append(j)
                    break
                j -= 1
            if i+1 > len(LSV):
                LSV.append(0)
        
        RSV = []
        for i in range(0,n-1):
            j = i + 1
            while j < n:
                if A[j] > A[i]:
                    RSV.append(j)
                    break
                j += 1
            if i+1 > len(RSV):
                RSV.append(0)
        RSV.append(0)
        max = 0
        for i in range(n):
            if LSV[i] * RSV[i] > max:
                max = LSV[i] * RSV[i]
        return max % (10**9 + 7)



A = Solution()
A.maxSpecialProduct([7,5,7,9,8,7])