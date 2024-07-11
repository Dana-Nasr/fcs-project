class Stack:
  def __init__(self):
    self.head = None
    self.size = 0
  def push(self, node):
    
    print("We are pushing:", node.user, "\n")

    node.next = self.head
    self.head = node
    self.size += 1