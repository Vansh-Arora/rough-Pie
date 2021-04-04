class Solution:
    def maxone(self, A, B):
        i,j = 0,0
        start = 0
        end = 0
        flips  = 0
        n = len(A)
        if n == 1:
            if flips < 1 and A[0] == 0:
                return 
            else:
                return [0]
        while end < n:
            if A[end] == 1 and flips <= B:
                if end == n-1:
                    if (end-start)+1 > (j-i)+1:
                        j = end
                        i = start
                end += 1
            elif A[end] == 0 and flips < B:
                if end == n-1:
                    if (end-start) > (j-i)+1:
                        j = end
                        i = start
                end += 1
                flips += 1

            else:
                if (end-start) > (j-i)+1:
                    j = end-1
                    i = start
                if A[start] == 0:
                    flips -= 1
                    start += 1
                else:
                    start += 1

        return [k for k in range(i,j+1)]

A = Solution()
print(A.maxone([0,0],4))