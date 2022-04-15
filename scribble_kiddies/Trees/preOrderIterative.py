# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def preorderTraversal(self, A):
        st = [A]
        ans = []
        while len(st) > 0:
            cur = st.pop()
            ans.append(cur.val)
            if cur.right:
                st.append(cur.right)
            if cur.left:
                st.append(cur.left)
        return ans

