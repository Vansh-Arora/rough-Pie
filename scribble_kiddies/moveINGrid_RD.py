#User function Template for python3
a = 0
class Solution:
    
    def helper(self,m,n,i,j):
        global a
        if i == m-1 and j == n-1:
            a += 1
            return
        if i >= m or j >= n:
            return
        self.helper(m,n,i+1,j)
        self.helper(m,n,i,j+1)
    def numberOfPaths(self, m, n):
        # code here 
        self.helper(m,n,0,0)
        return a


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m=int(m)
		n=int(n)
		ob = Solution();
		print(ob.numberOfPaths(m,n))

# } Driver Code Ends