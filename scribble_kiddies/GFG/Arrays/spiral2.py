class Solution:
	# @param A : integer
	# @return a list of list of integers
    def generateMatrix(self, A):
        M = [[-1 for i in range(A)] for i in range(A)]
        i = 0
        j = 0
        R = A-1
        C = A-1
        num = 1
        while i <= R and j <= C:
            for k in range(j,C+1):
                M[i][k] = num
                num += 1
            i += 1
            if i > R:
                break
            for k in range(i,R+1):
                M[k][C] = num
                num += 1
            C -= 1
            if j > C:
                break
            for k in range(C,j-1,-1):
                M[R][k] = num
                num += 1
            R -= 1
            if i > R:
                break
            for k in range(R,i-1,-1):
                M[k][j] = num
                num += 1
            j += 1
            if j > C:
                break
        return M
