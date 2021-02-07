class Solution:
    def findMin(n, indices):
        diff = []
        for i in indices:
            diff.append(abs(i-n))
        return min(diff)
    
    def shortestToChar(s,c):
        cIndex = []
        for i in range(len(s)):
            if s[i] == c:
                cIndex.append(i)
        answer = []
        for i in range(len(s)):
            diff = []
            for j in cIndex:
                diff.append(abs(i-j))
            answer.append(min(diff))
            
        return answer
print(Solution.shortestToChar("loveleetcode",'e'))