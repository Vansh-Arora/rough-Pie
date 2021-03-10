class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A = int(A)
        if A <= 1:
            return 0
        while(A>1):
            if A%2 == 0:
                A = A/2
            else:
                return 0
        return 1

A = Solution()
a = A.power('0')
print(0%2)
print(a)