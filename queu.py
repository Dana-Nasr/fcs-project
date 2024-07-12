class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    
  def displayNodes(self):
    current = self.head
    while current != None:
      print(current.data)
      current = current.next

  def inqueue(self, node):
    if self.size == 0:  
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
 
    self.size += 1
   

  def dequeue(self):
    if self.size == 0:
      print("\nYour Queue is empty! Enqueue first...\n")
    elif self.size == 1:
      current = self.head
      self.head = None
      self.tail = None
      self.size -= 1 
    else:
      current = self.head
      self.head = self.head.next
      current.next = None
      self.size -= 1
    return current