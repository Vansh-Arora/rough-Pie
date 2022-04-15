# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def lca(self, A, B, C):
        pathB = []
        cur = A
        flag = 0
        while cur or len(pathB) > 0:
            while cur:
                pathB.append(cur.val)
                if pathB[-1].val == B:
                    flag = 1
                    break
                cur = cur.left
            if flag: break
            cur = pathB.pop()
            cur = cur.right()
        pathC = []
        cur = A
        flag = 0
        while cur or len(pathC) > 0:
            while cur:
                pathC.append(cur.val)
                if pathC[-1].val == C:
                    flag = 1
                    break
                cur = cur.left
            if flag: break
            cur = pathC.pop()
            cur = cur.right()
        
        n = min(len(pathB),len(pathC))
        for i in range(n):
            if pathB[i] != pathC[i]:
                return pathB[i-1]
        



 