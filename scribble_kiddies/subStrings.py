class Solution:
    def helper(self,S,n,i,ans):
        if i == n:
            print(ans)
            return
        self.helper(S,n,i+1,ans)
        self.helper(S,n,i+1,ans+S[i])
        

    def genarate(self,S):
        self.helper(S,len(S),0,"")

A = Solution()
A.genarate("ABC")