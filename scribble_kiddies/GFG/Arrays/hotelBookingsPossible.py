class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        i = 0
        j = 0
        n = len(arrive)
        guests = 0
        arrive.sort()
        depart.sort()
        while i < n and j < n:
            if arrive[i] < depart[j]:
                guests += 1
                i += 1
                if guests > K:
                    return 0
            elif depart[j] < arrive[i]:
                guests -= 1
                j += 1
            else:
                i += 1
                j += 1
        return 1

