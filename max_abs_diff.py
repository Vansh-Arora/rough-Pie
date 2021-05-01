class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)
        ans  = 0
        for i in range(n):
            for j in range(i+1,n):
                temp = abs(A[i] - A[j]) + abs(i - j)
                if temp > ans:
                    ans = temp
        return ans
                
                
