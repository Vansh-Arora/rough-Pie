answer = []
class uniqueSubStrings:
    global answer
    def helper(self,S,n,i,ans):
        if i == n:
            if ans not in answer:
                answer.append(ans)
                print(ans)
            return
        self.helper(S,n,i+1,ans)
        self.helper(S,n,i+1,ans+S[i])
    

    def generate(self,S):
        self.helper(S,len(S),0,"")
    
A = uniqueSubStrings()
A.generate("AAA")