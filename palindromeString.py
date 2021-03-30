class Solution:
    def isPalindrome(self, A):
        B = ''
        for i in A:
            if ord(i.upper()) in range(65,92) or ord(i) in range(48,58):
                B += i.upper()
        j = -1
        for i in range(len(B)//2):
            if ord(B[i]) != ord(B[j]):
                return 0
            j -= 1
        return 1
                
                

a = Solution()
print(a.isPalindrome("1a b a ddaba2"))
