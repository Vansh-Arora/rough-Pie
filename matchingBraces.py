class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        st = []
        sym = ['+','-','*','/','(']
        for i in A:
            if i in sym:
                st.append(i)
            elif i == ")":
                if st[-1] == "(":
                    return 1
                else:
                    while st[-1] != "(":
                        st.pop()
                    st.pop()
        return 0
        
A = Solution()
print(A.braces('((a+b)+b+(A))'))