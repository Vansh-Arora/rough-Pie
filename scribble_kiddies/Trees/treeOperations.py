from platform import node


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
    return height + 1   ### Add 1 for root

## Function to get diameter of tree
## Diameter: Maximum distance between any 2 leaf nodes.
def getDiameter(node):
    if node ==  None:
        return 0
    ### 2 approaches
    ### if the diameter contains root (leftHeight + rightHeight + 1(for root))
    ### else diameter from left side or right side
    ### select whichever is max
    leftDim = getDiameter(node.left)
    rightDim = getDiameter(node.right)
    #print(leftDim,rightDim,(getHeight(node.left)+ getHeight(node.right) +1))
    return max(leftDim,rightDim,(getHeight(node.left,0)+ getHeight(node.right,0) +1))



## Function to count leaf nodes in a tree 
## if the current node has no children add 1 to count 
## else recurse for left and right
leafNodes = 0
def countLeaves(node):
    global leafNodes
    if node == None:
        return leafNodes
    if node.left == None and node.right == None:
        leafNodes+=1
        return leafNodes
    countLeaves(node.left)
    countLeaves(node.right)
    return leafNodes

## Function to count number of nodes in a tree
## if current node is present add 1
## recurse for left and right subtree
numOfNodes = 0
def countNodes(node):
    global numOfNodes
    if node ==  None:
        return numOfNodes
    numOfNodes += 1
    countNodes(node.left)
    countNodes(node.right)
    return numOfNodes



# Main 
if __name__ == "__main__":
    root = build()
    print(getHeight(root,0))
    print(getDiameter(root))
    print(countLeaves(root))
    print(countNodes(root))
