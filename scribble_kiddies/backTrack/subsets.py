class subsets:
    ans = []
    def generate(self,A,ANS,i,n):
        if i == n:
            self.ans.append(ANS)
            print(ANS)
            return
        ANS.append(A[i])
        self.generate(A,ANS,i+1,n)
        ANS.pop()
        self.generate(A,ANS,i+1,n)

A = subsets()
A.generate([1,2,3],[],0,3)
print(A.ans)
        