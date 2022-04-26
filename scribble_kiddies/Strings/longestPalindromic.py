class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        def check(A,st,en):
            L,R=st,en
            while L>=0 and R<len(A) and A[L]==A[R]:
                L -= 1
                R += 1
            return R-L-1
        start = 0
        end = 0
        for i in range(len(A)):
            len1 = check(A,i,i)
            len2 = check(A,i,i+1)
            len_ = max(len1,len2)
            if len_ > end-start:
                #print(end,start,end-start,"Before")
                start = i - (((len_-1)//2))
                end = i + len_//2+1
                #print(start,end,A[start:end],len_)
            #print(start,end)
        return A[start:end]