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

def createList(nodes,edges):
    adjList = [None for i in range(nodes)]
    for i in range(nodes):
         adjList[i] = singlyLinkedList()
    for i in range(edges):
        node1 = int(input("Enter node A data: "))
        node2 = int(input("Enter node B data: "))
        adjList[node1].addNode(node2)
        adjList[node2].addNode(node1)
    return adjList
    
def printList(adjList,nodes):
    for i in range(nodes):

        print(i,end="->")
        curr = adjList[i].head
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("X")

if __name__ == "__main__":
    adjList = createList(7,7)
    printList(adjList,7)