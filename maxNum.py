from functools import cmp_to_key
class Solution:

    
    def largestNumber(self, A):
        ans = ''
        M = max(A)
        max_len = len(str(M))
        
        num = [str(i) for i in A]
        key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
        num.sort(key=key)
        num.reverse()
        for i in num:
            ans = ans + i
        #print(num)
        if int(ans) == 0:
            return 0
        return(ans)

A = Solution()
ar = input().split()
ar = [int(i) for i in ar]
A.largestNumber(ar)