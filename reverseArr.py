class Solution:
    def arrange(self, A):
        n = len(A)
        a = [i for i in A]
        for i in range(n):
            A[i] = a[a[i]]
        return(A)



A = Solution()
x = input().split()
x = [int(i) for i in x]
a = A.arrange(x)
print(a)