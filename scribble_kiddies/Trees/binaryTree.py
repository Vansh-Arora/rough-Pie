

class Node:
    # Structure of Node
    def __init__(self):
        self.left = None
        self.right = None
        self.data = data
    
# Building a Tree
def build(parent,ilc):
    ## ilc: is left child present??

    ## If the tree is initially empty,
    ## so parent will be none
    ## thus we set the first node as root
    
    if parent == None:
        print("Enter root Node data.")
    elif ilc:
        print("Enter left child data for {}".format(parent.data))
    else:
        print("Enter right child data for {}".format(parent.data))

    # create and take input for new node
    val = int(input())
    newNode =  Node(val)

    # now building forward the new node
    
    print("{} has left child?".format(newNode.data))

    hlc = int(input())    # has left child??
    if hlc:
        newNode.left = build(newNode,True)
    
    print("{} has right child?".format(newNode.data))

    hrc = int(input())    # has right child??
    if hrc:
        newNode.right = build(newNode,False)   

    return newNode

def preOdisplay(node):
    if node == None:
        return
    result = ""
    if node.left == None:
        result += '.' + "<-" + str(node.data) + "->"
    else:
        result += str(node.left.data) + "<-" + str(node.data) + "->"
    if node.right == None:
        result += '.'
    else:
        result += str(node.right.data)
    print(result)
    preOdisplay(node.left)
    preOdisplay(node.right)

def postOdisplay(node):
    if node == None:
        return
    result = ""
    if node.left == None:
        result += '.' + "<-" + str(node.data) + "->"
    else:
        result += str(node.left.data) + "<-" + str(node.data) + "->"
    if node.right == None:
        result += '.'
    else:
        result += str(node.right.data)
    postOdisplay(node.left)
    postOdisplay(node.right)
    print(result)

def inOdisplay(node):
    if node == None:
        return
    result = ""
    if node.left == None:
        result += '.' + "<-" + str(node.data) + "->"
    else:
        result += str(node.left.data) + "<-" + str(node.data) + "->"
    if node.right == None:
        result += '.'
    else:
        result += str(node.right.data)
    inOdisplay(node.left)
    print(result)
    inOdisplay(node.right)



root = build(None,0) 
preOdisplay(root)
print()
inOdisplay(root)
print()
postOdisplay(root)
print()


        


