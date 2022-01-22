class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data

def build():
    data = int(input())
    if data == -1:
        return None
    nn = Node(data)
    nn.left = build()
    nn.right = build()
    return nn

def Mirror(node):
    if node == None:
        return
    node.left,node.right = node.right,node.left
    Mirror(node.left)
    Mirror(node.right)


def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(node.data,end=" ")
    inOrder(node.right)


root = build()
Mirror(root)
inOrder(root)