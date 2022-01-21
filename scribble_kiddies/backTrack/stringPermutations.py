class stringPermutations:
    def generate(self,S,ans,i):
        if i == len(S):
            print(ans)
            return
        for j in range(i,len(S)):
            S[j],S[i] = S[i],S[j]
            self.generate(S,ans+S[i],i+1)
            S[j],S[i] = S[i],S[j]
A = stringPermutations()
A.generate(['A','B','C'],"",0)
