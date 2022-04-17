class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        R = len(A) - 1
        C = len(A[0]) - 1
        i = 0
        j = 0
        ans = []
        
        while i <= R and j <= C:
            for k in range(j,C+1):
                ans.append(A[i][k])
            i += 1
            if i > R:
                break
            
            for k in range(i,R+1):
                ans.append(A[k][C])
            C -= 1
            if j > C:
                break
            
            for k in range(C,j-1,-1):
                ans.append(A[R][k])
            R -= 1
            if i > R:
                break
            for k in range(R,i-1,-1):
                ans.append(A[k][j])
            j += 1
            if j > C:
                break
        return ans