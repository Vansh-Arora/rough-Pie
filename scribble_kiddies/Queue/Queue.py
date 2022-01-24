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
    
if __name__ == "__main__":
    Que = Queue()
    Que.fillQueue()
    Que.display()
    print(Que.deQueue())