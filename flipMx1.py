class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        if '0' not in A:
            return []
        ans = [-1,-1]
        n = len(A)
        start = 0
        end = -1
        count = 0
        temp = 0
        for i in range(n):
            if A[i] == '0':
                if temp < 0:
                    start = i
                    end = i
                    temp = 0
                else:
                    end += 1  
                temp += 1
            

            elif A[i] == '1':
                if temp > count:
                    count = temp
                    ans[0] = start
                    ans[1] = end
                    end += 1
                    temp -= 1
                    
                elif temp > 0:
                    temp -= 1
                    end += 1
                elif temp == 0:
                    temp -= 1

        if temp > count:
            count = temp
            ans[0] = start
            ans[1] = end
        ans[0] += 1
        ans[1] += 1
        return ans
A = Solution()

print(A.flip('01010'))