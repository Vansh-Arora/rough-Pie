# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root.right != None:
            (self.convertBST(root.right))
            if root.right.val > self.temp:
                root.val = self.temp + root.val
            else:
                root.val = root.right.val + root.val

        if root.left != None:
            root.left.val = root.val + root.left.val
            (self.convertBST(root.left))
        if root.left == None and root.right == None :
            print(root)

        return root