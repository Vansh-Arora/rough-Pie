# Works only if tree has both nodes present
def lca(root,n1,n2):
    if root == None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    lefty = lca(root.left,n1,n2)
    righty = lca(root.right,n1,n2)
    if lefty != None and righty != None:
        return root
    if lefty != None:
        return lefty
    else:
        return righty