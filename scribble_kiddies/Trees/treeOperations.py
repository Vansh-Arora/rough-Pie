class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.rear == -1 or self.front>self.rear:
            return True
        
        return False
    
    def enQueue(self,data):
        if self.front == -1:
            self.front += 1
        self.rear += 1
        self.q.append(data)
    
    def deQueue(self):
        if self.front == -1 or self.front > self.rear:
            return None
        self.front += 1
        return self.q[self.front - 1]
    
    def peek(self):
        if self.front == -1 or self.front > self.rear:
            return None
        return self.q[self.front]

    def display(self):
        i = self.front
        while i<=self.rear:
            if self.q[i] != None:
                print(self.q[i].data)
            else:
                print(self.q[i])
            i += 1

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


## Function to print level order traversal of a tree
Que = Queue()
def traverse(node):
    Que.enQueue(node)
    Que.enQueue(None)
    while not Que.isEmpty():
        curr = Que.deQueue()
        if curr == None:
            if Que.front >= Que.rear:
                break
            Que.enQueue(None)

        else:
            print(curr.data)
            if curr.left:
                Que.enQueue(curr.left)
            if curr.right:
                Que.enQueue(curr.right)


## Function to take sum of nodes on a level
sum = 0
QueForSum = Queue()
def levelSum(node):
    global sum
    QueForSum.enQueue(node)
    QueForSum.enQueue(None)
    while not QueForSum.isEmpty():
        curr = QueForSum.deQueue()
        if curr == None:
            print(sum)
            sum = 0
            if QueForSum.front >= QueForSum.rear:
                break
            QueForSum.enQueue(None)
        else:
            sum += curr.data
            if curr.left:
                QueForSum.enQueue(curr.left)
            if curr.right:
                QueForSum.enQueue(curr.right)  

## Function to print left view of a tree

def leftView(node):
    if node == None:
        return
    traverse(node)
    Que.front = 0
    curr = Que.deQueue()
    print(curr.data)
    i = Que.front
    curr = Que.deQueue()
    while i < Que.rear:
        if curr == None:
            curr = Que.deQueue()
            i += 1
            print(curr.data)
            continue
        else:
            curr = Que.deQueue()
            i += 1

## Function to print right view of a tree
def rightView(node):
    if node == None:
        return
    traverse(node)
    Que.front = 0
    i = 1
    curr = Que.deQueue()
    while i <= Que.rear:
        if Que.peek() == None:
            print(curr.data)
            curr = Que.deQueue()
            i += 1
        else:
            curr = Que.deQueue()
            i += 1



def traverse2(root):
    q = []
    if root:
        q.append(root)
        q.append(None)
        start = 0
        end = 1
    while q[start] != None or start < end:
        cur = q[start]
        start += 1
        if cur == None:
            q.append(None)
            end += 1
        else:
            if cur.left:
                q.append(cur.left)
                end += 1
            if cur.right:
                q.append(cur.right)
                end += 1
    print(q)
            

# Main 
if __name__ == "__main__":
    root = build()
    print(getHeight(root,0))
    #print(getDiameter(root))
    print(countLeaves(root))
    #traverse(root)
    #levelSum(root)
    #print(countNodes(root))
    #leftView(root)
    rightView(root)
    traverse2(root)
