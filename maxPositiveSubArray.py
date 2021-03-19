class Solution:
    def maxset(self, A):
        initial = 0
        sol = {}
        sum = 0
        for i in range(len(A)):

            if A[i] < 0:
                final = i-1
                count = final+1 - initial
                if sum in sol:
                    if count > max(sol[sum]):
                        sol[sum][count] = [initial,final]
                else:
                    sol[sum] = {count: [initial,final]}
                sum = 0
                initial = i+1

            elif(i == len(A) - 1):
                sum = sum + A[i]
                final = i
                count = final+1 - initial
                if sum in sol:
                    if count > max(sol[sum]):
                        sol[sum][count] = [initial,final]
                else:
                    sol[sum] = {count: [initial,final]}

            else:
                sum += A[i]

        ans = sol[max(sol)]
        ansf = ans[max(ans)]
        return(A[ansf[0]:ansf[1]+1])

a = Solution()
a.maxset([1,2,3,4,-5,10,-7,6,3,-1,-2,0,1,2,3,4])
print(a.maxset([1,2,3,-5,5,1]))
#a.maxset([1,2,3])