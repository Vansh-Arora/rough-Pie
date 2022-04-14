def inOrder(root):
    stck = [root]
    ans = []
    cur = root.left
    while cur or len(stck) > 0:
        while cur != None:
            stck.append(cur)
            cur = cur.left
        cur = stck.pop()
        ans.append(cur.data)
        cur = cur.right
    print(ans)
            