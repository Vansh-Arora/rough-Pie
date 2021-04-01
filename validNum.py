import re
class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        A = A.strip()
        pattern = r"^[\-\+]?[0-9]*\.?[0-9]+$|^[\-\+]?[0-9]*\.?[0-9]e[\-\+]?[0-9]+$"
        result = (re.search(pattern,A))
        return int(result != None)

A = Solution()
a = A.isNumber(input())
print(a)