class Solution:
    def isPalindrome(self, A):
        
        i = 0
        A = str(A)
        j = len(A) - 1

        while i<len(A)//2 and j >= len(A)//2:
            if (A[i]) != (A[j]):
                return 0
            i += 1
            j -= 1
        return 1

    def solve(self, A):
        n0 = len(A)
        n =len(A)+1
        while(not self.isPalindrome(A[:n-1])):
            n -= 1
        return n0 - (n-1)
A = Solution()
a = A.solve('abcdeffedcbabc')
print(a)