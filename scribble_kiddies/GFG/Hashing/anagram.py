def Anagrams(words):
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
