class Solution:
    def findLHS(self, nums: List[int]) -> int:
        lengthArray = [] # Array to store length of different series occuring in a test case
        nums = sorted(nums) # Sorting list before creating dictionary
        
        # Now dictionary will have all sorted elements
        numsDict = {}   # To count numbers and their occurence
        # Storing nums in numsDict(dictionary)
        for i in nums:
            if i in numsDict:
                numsDict[i] += 1
            else:
                numsDict[i] = 1

        for i in numsDict.keys():
            length = 0    # To store the length of a series
            if(i + 1) in numsDict.keys():   # Look only for immediate successors
                length = numsDict[i] + numsDict[i+1]
            lengthArray.append(length)

        return max(lengthArray)