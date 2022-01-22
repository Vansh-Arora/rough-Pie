class Node:
    def __init__(self,data):
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

def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(node.data,end=" ")
    inOrder(node.right)

def preOrder(node):
    if node == None:
        return
    print(node.data,end=" ")
    preOrder(node.left)
    preOrder(node.right)

def postOrder(node):
    if node == None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.data,end=" ")


root = build()

preOrder(root)
print()
inOrder(root)
print()
postOrder(root)
print()

