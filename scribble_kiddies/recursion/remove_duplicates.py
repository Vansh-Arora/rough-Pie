alpha = {}
class Solution:
    def helper(self,S,n,i,ans):
        global alpha
        if i == n:
            return ans
        if alpha[S[i]] == 0:
            ans += S[i]
            alpha[S[i]] = 1
            return self.helper(S,n,i+1,ans)

        return self.helper(S,n,i+1,ans)
            

        

    def remove(self,S):
        global alpha
        for i in range(97,123):
            alpha[chr(i)] = 0
        return self.helper(S,len(S),0,"")

S = Solution()
print(S.remove("samaa"))
    