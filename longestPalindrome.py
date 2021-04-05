class Solution:
    def longestPalindrome(self, A):
       maxlen = 1
       beg = 0
       start = 0
       end = 0
       n = len(A)
       for i in range(1,n):
           start = i - 1
           end = i
           while start >= 0 and end < n and A[start] == A[end]:
               if maxlen < (end - start) + 1:
                   maxlen = (end - start) + 1
                   beg = start
               start -= 1
               end += 1
           start = i-1
           end = i+1
           while start >= 0 and end < n and A[start] == A[end]:
               if maxlen < (end - start) + 1:
                   maxlen = (end - start) + 1
                   beg = start
               start -= 1
               end += 1
       return A[beg:maxlen+beg]
A = Solution()
print(A.longestPalindrome("rofgeeksskeegfor"))   
