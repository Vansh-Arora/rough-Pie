class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        M = 10**6
        start = 0
        while start <= M:
            mid = (start + M)//2
            if mid**2 == A:
                return mid
            elif mid**2 < A:
                start = mid+1
            else:
                M = mid-1
        if mid**2 > A:
            return mid-1
        else:
            return mid
A = Solution()
print(A.sqrt(5))
