class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        ans = 0
        n = len(A)
        i = 1
        prevx = A[0]
        prevy = B[0]
        while i < n:
            curx = A[i]
            cury = B[i]
            ans += max(abs(prevx-curx),abs(prevy-cury))
            prevx = curx
            prevy = cury
            i += 1
        return ans
