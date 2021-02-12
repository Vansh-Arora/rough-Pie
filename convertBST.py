# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def convert(self, root: TreeNode) -> TreeNode:
        print(self.sum)
        if root == None:
            return
        self.convert(root.right)
        self.sum = self.sum + root.val
        root.val = self.sum
        self.convert(root.left)
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.convert(root)
        return root