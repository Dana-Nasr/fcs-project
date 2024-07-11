class LinkedList:

   def __init__(self):
    self.head = None
    self.size = 0
  
   def addNode(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.size += 1