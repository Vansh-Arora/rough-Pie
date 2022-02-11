#User function Template for python3
inO = []
def inOrder(root,key):
    global inO
    if root == None:
        return root
    if len(inO) != 0 and inO[-1].data == key:
        return root
    inO.append(root)
    inOrder(root.right,key)
#Function to delete a root from BST.
def deleteroot(root, X):
    # code here.
    
    if root == None:
        return
    if X > root.data:
        deleteroot(root.right,X)
    if X < root.data:
        deleteroot(root.left,X)
    else:
        if root.left==None and root.right == None:
            root = None
            return
        if root.left == None:
            root = root.right
            root.right = None
            return
        if root.right == None:
            root = root.left
            root.left = None
            return
        delN = inOrder(root,X)
        root.data = delN.data
        deleteroot(root.right,delN.data)
        