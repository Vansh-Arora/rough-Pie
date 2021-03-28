class Solution:
    def solve(self, A):
        ans  =[]
        for i in range(A):
            ans.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                     ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j] + ans[i-1][j-1])
        return ans

A = Solution()
a = A.solve(0)
print(a)