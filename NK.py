class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        min = 10**(B-1)
        max = 9 * (11**(B-1))
        ans = []
        print(min,max,sep=' ')
        for i in A:
            if i in range(min,max+1) and i < C:
                ans.append(i)
        print(ans)
        return ans
        

a = Solution()
a.solve([0,1,5],1,2)