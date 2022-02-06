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
    
    def createList(self,n):
        for i in range(n):
            self.addNode(int(input("Enter node data: ")))


    def printList(self):
        curr = A.head
        while(curr):
            print(curr.data,end='->')
            curr = curr.next
        print("X")
        
A = singlyLinkedList()
A.createList(int(input("Enter size of list: ")))
A.printList()

