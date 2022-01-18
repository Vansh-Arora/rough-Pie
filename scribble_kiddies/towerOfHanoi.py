# User function Template for python3
steps = 0
class Solution:
    def toh(self, N, fromm, to, aux):
        global steps
        # Your code here
        if N==1:
            print("move disk {} from rod {} to rod {}".format(N,fromm,to))
            steps += 1
            return steps
        else:
            self.toh(N-1,fromm,aux,to)
            print("move disk {} from rod {} to rod {}".format(N,fromm,to))
            steps+= 1
            self.toh(N-1,aux,to,fromm)
        return steps
        

#{ 
#  Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends