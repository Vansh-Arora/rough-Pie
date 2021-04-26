class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        st = A
        n = len(st)
        longest = 0
        for i in range(n):
            temp = ''
            for j in range(i,n):
                if st[j] not in temp:
                    temp += st[j]
                else:
                    if len(temp) > longest:
                        longest = len(temp)
                    temp = ''
                    break
            if len(temp) != 0 and len(temp)>longest:
                return (len(temp))
                
        return longest
