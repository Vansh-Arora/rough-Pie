class Solution:
    def pow(self, x, n):
        if n == 1:
            return x
        elif n%2 == 0:
            return pow(x*x,n//2)
        else:
            return x*pow(x*x,n//2)

A = Solution()
#print(A.pow(71045970,41535484,64735492))
print(A.pow(40,9))