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

def createList(nodes):
    adjList = [None for i in range(nodes)]
    for i in range(nodes):
         adjList[i] = singlyLinkedList()
    