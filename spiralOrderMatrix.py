class Solution:
    def SpiralOrder(self,A):
        ans = []
        dir = 0
        T = 0
        L = 0
        B = len(A) - 1
        R = len(A[0]) - 1
        while(T <= B and L <= R):
            if dir == 0:
                for i in range(L,R+1):
                    ans.append(A[T][i])
                T += 1
                dir = 1
            elif dir == 1:
                for i in range(T,B+1):
                    ans.append(A[i][R])
                R -= 1
                dir = 2
            elif dir == 2:
                for i in range(R,L-1,-1):
                    ans.append(A[B][i])
                B -= 1
                dir = 3
            elif dir == 3:
                for i in range(B,T-1,-1):
                    ans.append(A[i][L])
                L += 1
                dir = 0
        return ans
a = Solution()
print(a.SpiralOrder([[ 1, 2 ], [ 3, 4 ], [ 5,6 ]]))