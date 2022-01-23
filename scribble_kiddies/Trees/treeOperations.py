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
#height = 0
def getHeight(node,height):
    #global height
    if node == None:
        return height
    leftHt = getHeight(node.left,height)
    rightHt = getHeight(node.right,height)
    height =  max(leftHt,rightHt)
    return height + 1

def getDiameter(node):
    if node ==  None:
        return 0
    leftDim = getDiameter(node.left)
    rightDim = getDiameter(node.right)
    #print(leftDim,rightDim,(getHeight(node.left)+ getHeight(node.right) +1))
    return max(leftDim,rightDim,(getHeight(node.left,0)+ getHeight(node.right,0) +1))
count = 0
def countLeaves(node):
    global count
    if node == None:
        return count
    if node.left == None and node.right == None:
        count+=1
        return count
    countLeaves(node.left)
    countLeaves(node.right)
    return count
if __name__ == "__main__":
    root = build()
    print(getHeight(root,0))
    print(getDiameter(root))
    print(countLeaves(root))
