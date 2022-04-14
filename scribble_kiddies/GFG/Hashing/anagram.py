class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        dis = {}
        for i in words:
            temp = "".join(sorted(i))
			if temp not in dis:
				dis[temp] = [i]
			else:
				dis[temp].append(i)
		ans = []
		for i in dis:
			ans.append(dis[i])
		return ans
