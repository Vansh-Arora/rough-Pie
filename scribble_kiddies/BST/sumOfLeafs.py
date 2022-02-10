def sumOfLeafNodes(root):
    if root==None:
        return 0
    if root.left==None and root.right==None: 
        return root.data
        
    return sumOfLeafNodes(root.left) + sumOfLeafNodes(root.right)