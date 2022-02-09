# Linked List
class singlyLinkedListNode:
    def __init__(self,data):
        self.next = None
        self.data = data
class singlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self,data):
        node = singlyLinkedListNode(data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

## Create adjacency list
def createList(nodes,edges):
    adjList = [None for i in range(nodes)]
    for i in range(nodes):
         adjList[i] = singlyLinkedList()
    for i in range(edges):
        node1 = int(input("Enter start node data: "))
        node2 = int(input("Enter end node data: "))
        adjList[node1].addNode(node2)
    return adjList

