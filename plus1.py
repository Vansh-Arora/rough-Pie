'''
class Solution:
    def plusOne(self, A):
        num = 0
        j = 0
        for i in range(len(A)-1,-1,-1):
            num += 10**j * A[i]
            j += 1
        num += 1
        num = [int(i) for i in str(num)]
        return num
A = Solution()
A.plusOne([0,1,2,3])
'''
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        i = 0
        while A[i] == 0 and i < n-1:
            i += 1
        ans = []
        while i < n:
            if i == n-1:
                ans.append(A[i] + 1)
            else:
                ans.append(A[i])
        return ans


class Solution:
    def plusOne(self, A):
        c = 1
        for i in range(len(A)-1,-1,-1):
            if c > 0:
                if A[i] == 9:
                    A[i] = 0
                    c = 1
                else:
                    A[i] += 1
                    c = 0
        if c == 1:
            A = [1] + A
        i = 0
        while i < len(A) and A[i] == 0:
            i += 1
        A = A[i:]
        return (A)
'''

class Solution:
    def plusOne(self, A):
        c = 1
        i = -1
        while c != 0 and i >= -len(A):
            if A[i] == 9:
                A[i] = 0
            else:
                A[i] += 1
                c = 0
            i -= 1
        if c != 0:
            A = [1] + A
        i = 0
        while i < len(A) and A[i] == 0:
            i += 1
        A = A[i:]
        return (A)
A = Solution()
print(A.plusOne([9,9,9]))