class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        maxi = max(A)
        nums = {i:0 for i in range(1,maxi+1)}
        ans = max(maxi,0)
        for i in A:
            if i > 0:
                nums[i] += 1
        for i in nums:
            if nums[i] == 0:
                return i
        return ans+1
        