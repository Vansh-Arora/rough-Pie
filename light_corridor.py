class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        lights = []
        i = 0
        prev = -1
        while i<n:
            i = i + B - 1
            if i < n:
                if A[i] == 1:
                    lights.append(i)
                    prev = i
                    i = i + B
                else:
                    while(i > prev and A[i] == 0):
                        i = i - 1
                    if i == prev:
                        return -1
                    lights.append(i)
                    i = i + B
            else:
                i = n-1
                while(i>prev and A[i] == 0):
                    i -= 1
                if i == prev:
                    return -1
                lights.append(i)
                break
        return len(lights)

A = Solution()
print(A.solve([1,1,1,0,0,0,1,1,1],1))