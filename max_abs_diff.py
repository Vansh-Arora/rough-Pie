class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        n = len(A)
        ans  = 0
        for i in range(1,n):
            for j in range(i):
                print(i,j,sep=" ")
                temp = abs(A[i] - A[j]) + abs(i - j)
                if temp > ans:
                    ans = temp
        return ans
                
                
A = Solution()
print(A.maxArr([1, 3, -1]))