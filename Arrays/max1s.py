class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tempCount = 0
        count = 0
        for i in nums:
            if i == 1:
                tempCount += 1
            else:
                if tempCount > count:
                    count = tempCount
                tempCount = 0
        if tempCount > count:
            count = tempCount
        return count        