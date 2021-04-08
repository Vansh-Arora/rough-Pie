class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):

        st = []
        for i in A:
            if i not in '+-*/':
                st.append(i)
            else:
                st.append(int(eval("{2}{1}{0}".format(st.pop(),i,st.pop()))))
        return st[0]
