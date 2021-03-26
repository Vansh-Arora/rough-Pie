import re
class Solution:
    # @param A : string
    # @return an integer
    def isIP(self, A):
        A = A.strip()
        #pattern = r"^[0-1]?[0-9]?[0-9]$|^2[0-4][0-9]$|^25[0-5]$"
        pattern = r"(^[0-1]?[0-9]?[0-9]|^2[0-4][0-9]|^25[0-5])\.([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$"
        result = (re.search(pattern,A))
        return int(result != None)
    def restoreIpAddresses(self,A):
        n = len(A)
        if n>12:
            while len(A)>12 and A[0] == '0':
                A = A[1:]
        n = len(A)
        if n>12:
            return
        else:
            ans = []
            if n<4:
                return
            else:
                snew = A
                for i in range(1, n - 2):
                    for j in range(i + 1, n - 1):
                        for k in range(j + 1, n):
                            snew = snew[:k] + "." + snew[k:]
                            snew = snew[:j] + "." + snew[j:]
                            snew = snew[:i] + "." + snew[i:] 
                            if self.isIP(snew):
                                ans.append(snew)
                            snew = A
                return ans
                              

                




A = Solution()
a = A.restoreIpAddresses(input())
#a = A.isIP('1.234.56.78')
print(a)