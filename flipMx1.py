class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        i = 0 
        j = 0
        ans  = []
        count = 0
        n = len(A)
        while j < n:
            if i == j and A[i] == 1:
                i += 1
                j += 1
            elif A[j] == 0:
                count += 1
                ans[0] = i
                ans[1] = j
                j += 1
            elif A[j] == 1:
                if count > 0:
                    count -= 1
                else:
                    count = 0
                    i = j
            j += 1
        return ans

A = Solution()
print(A.flip('0011010000100000'))
                
                