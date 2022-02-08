# Linked List

from inspect import BlockFinder


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
    adjList = [None for i in range(nodes)]
    for i in range(nodes):
         adjList[i] = singlyLinkedList()
    for i in range(edges):
        node1 = int(input("Enter node A data: "))
        node2 = int(input("Enter node B data: "))
        adjList[node1].addNode(node2)
        adjList[node2].addNode(node1)
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

# Breadth First Search
def BFS(adjList):
    Q = Queue()
    Q.enQueue(0)
    visited = [0 for i in range(len(adjList))]
    visited[0] = 1
    while not Q.isEmpty():
        currNode = Q.deQueue()
        print(currNode,end = " ")
        curr = adjList[currNode].head
        while curr:
            if not visited[curr.data]:
                visited[curr.data] = 1
                Q.enQueue(curr.data)
            curr = curr.next

def DFS(adjList):
    ST = []
    visited = [0 for i in range(len(adjList))]
    visited[0] = 1
    ST.append(0)
    print(0,end = " ")
    curr = adjList[0].head
    while len(ST) != 0:
        if curr and not visited[curr.data]:
                ST.append(curr.data)
                print(curr.data,end=" ")
                visited[curr.data] = 1
                curr = adjList[curr.data].head
        else:
            if curr.next:
                curr = curr.next
            else:
                ST.pop()
                if len(ST) > 0:
                    curr = adjList[ST[-1]].head




    


if __name__ == "__main__":
    nodes = int(input("Enter Number of Nodes: "))
    edges = int(input("Enter Number of edges: "))
    adjList = createList(nodes,edges)
    printList(adjList,7)
    BFS(adjList)
    print()
    DFS(adjList)