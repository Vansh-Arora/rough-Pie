## Iterative
def flatten(root):
    cur = root
    while cur:
        if cur.left:
            temp = cur.right
            cur.right = cur.left
            cur.left = None
            curr = cur
            while curr.right:
                curr = curr.right
            curr.right = temp
            cur = cur.right
        else:
            cur = cur.right
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