class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countList = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                countList.append(count)
                count = 0
        if countList != []:
            return max(countList)
        else:
            return 0
        