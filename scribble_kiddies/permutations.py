class Solution:
    def helper(self,S,ans):
        if len(S) <= 0:
            print(ans)
            return
        for i in range(len(S)):
            self.helper(S[:i]+S[i+1:],ans+S[i])

    def generate(self,S):
        return self.helper(S,"")
A = Solution()
A.generate("ABC")