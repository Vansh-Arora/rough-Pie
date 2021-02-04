class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ansL = []
        for i in range(len(nums)):
            ans = 0
            curr = nums.count(nums[i])
            if(nums[i] + 1) in nums:
                successor = nums.count(nums[i] + 1)
                ans = curr + successor
            elif(nums[i] - 1) in nums:
                predecessor = nums.count(nums[i] - 1)
                ans = predecessor + curr
            ansL.append(ans)
        return max(ansL)