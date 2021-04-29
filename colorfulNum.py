class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        num = str(A)
        n = len(num)
        if '1' in num and n>1:
            return 0
        prod = []
        
        for i in range(n):
            for j in range(0,n-i):
                temp = num[j:j+i+1]
                p = 1
                for x in temp:
                    p = p * int(x)
                if p in prod:
                    return 0
                else:
                    prod.append(p)
        return 1

A = Solution()
print(A.colorful(23))