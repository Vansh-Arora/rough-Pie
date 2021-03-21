class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A>=0:
            i = 0
            A = str(A)
            j = len(A) - 1

            while i<len(A)//2 and j >= len(A)//2:
                if int(A[i]) != int(A[j]):
                    return 0
                i += 1
                j -= 1
            return 1
        else:
            return 0

a = Solution()
print(a.isPalindrome(2147447412))