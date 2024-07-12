class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def getSize(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.next
        return size
    
    def inqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return None
        removed_node = self.head
        self.head = self.head.next
        removed_node.next = None  
        return removed_node
    
    def displayNodes(self):
        current = self.head
        while current is not None:
            print(current.user.id)
            current = current.next
