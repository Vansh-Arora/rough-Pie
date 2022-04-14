class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
		dis = {}
		for i in range(len(A)):
			temp = 0
			for j in A[i]:
				temp += (ord(j)*ord(j))
			if temp not in dis:
				dis[temp] = [i+1]
			else:
				dis[temp].append(i+1)
		ans = []
		for i in dis:
			ans.append(dis[i])
		return ans

		
