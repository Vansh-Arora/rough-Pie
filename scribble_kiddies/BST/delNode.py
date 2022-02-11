def minVal(root,key):
    curr = root
    while curr.left:
        curr = curr.left
    return curr 
#Function to delete a root from BST.
def deleteNode(root, X):
    # code here.
    
    if root == None:
        return root
    if X > root.data:
        root.right = deleteNode(root.right,X)
    elif X < root.data:
        root.left = deleteNode(root.left,X)
    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp
        temp = minVal(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.data)
        