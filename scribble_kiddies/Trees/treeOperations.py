class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data

## Build tree
def build():
    data = int(input())
    if data == -1:
        return None
    nn = Node(data)
    nn.left = build()
    nn.right = build()
    return nn

## Print inOrder Traversal
def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(node.data,end=" ")
    inOrder(node.right)


## Calculate height of tree
height = 0
def getHeight(node):
    global height
    if node == None:
        return height
    leftHt = getHeight(node.left)
    rightHt = getHeight(node.right)
    height =  max(leftHt,rightHt)
    return height + 1


if __name__ == "__main__":
    root = build()
    print(getHeight(root))
