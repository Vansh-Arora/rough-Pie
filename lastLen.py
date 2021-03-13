class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        A = A.rstrip()
        i = -1
        j = 0
        while(i >= -len(A)):
            if A[i] == " ":
                return j
            else:
                i -= 1
                j += 1
        return len(A)
                
A = Solution()
a = A.lengthOfLastWord('hello ')
print(a)