'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        sum = 0
        maxYet = min(A) - 4
        for each in A:
            sum += each
            if sum < each:
                sum = each
            if maxYet < sum:
                maxYet = sum
        return maxYet
                
'''
inf = float('inf')

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxSubArray(self, A):
	    best = -inf
	    sumsofar = 0
	    for x in A:
	        sumsofar += x
	        best = max(sumsofar, best)
	        # Doing this last, to handle case
	        # when all numbers are negative.
	        sumsofar = max(sumsofar, 0)
	    return best
a = Solution()
print(a.maxSubArray([100,200,300,-200,400,-1800,1500]))