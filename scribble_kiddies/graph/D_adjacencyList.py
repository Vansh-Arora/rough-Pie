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
# Queue
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
    
    def display(self):
        i = self.front
        while i<=self.rear:
            print(self.q[i])
            i += 1

    def fillQueue(self):
        val = input()
        while val != '-1':
            self.enQueue(val)
            val = input()

## Create adjacency list
def createList(nodes,edges):
    global indeg
    adjList = [None for i in range(nodes)]
    for i in range(nodes):
         adjList[i] = singlyLinkedList()
    for i in range(edges):
        node1 = int(input("Enter start node data: "))
        node2 = int(input("Enter end node data: "))
        adjList[node1].addNode(node2)
        indeg[node2] += 1
    return adjList

## Print List
def printList(adjList,nodes):
    for i in range(nodes):
        print(i,end="->")
        curr = adjList[i].head
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("X")
def TopologicalSort(adjList):
    count = 0
    Q = Queue()
    for i in range(len(indeg)):
        if indeg[i] == 0:
            Q.enQueue(i)
    while not Q.isEmpty():
        currentNode = Q.deQueue()
        print(currentNode,end="->")
        curr = adjList[currentNode].head
        while curr:
            indeg[curr.data] -= 1
            if indeg[curr.data] == 0:
                Q.enQueue(curr.data)
            curr = curr.next

            

if __name__ == "__main__":
    nodes = int(input("Enter Number of Nodes: "))
    edges = int(input("Enter Number of edges: "))
    indeg = [0 for i in range(nodes)]

    adjList = createList(nodes,edges)
    printList(adjList,7)
    print()
    print(indeg)
    TopologicalSort(adjList)