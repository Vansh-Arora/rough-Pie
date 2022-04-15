## Iterative
def flatten(A):
    root = A
    while root:
        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None
            curr = root
            while curr.right:
                curr = curr.right
            curr.right = temp
        root = root.right
    return root

## Recursively
'''
def flatten(root):
    if root == None:
        return
    right = root.right
    root.right = root.left
    root.left = None
    curr = root
    while curr.right:
        curr = curr.right
    curr.right = right
    flatten(root.right)
'''