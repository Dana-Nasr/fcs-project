class queue:
 def __init__(self):
    self.head = None
    self.tail = None
 def getSize(self):
    current = self.head
    size = 0
    while current != None:
      size += 1
      current = current.next
    return size
 def inqueue(self, node):
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node          #repositioning tail