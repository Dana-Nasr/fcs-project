class Stack:
  def __init__(self):
    self.head = None
    self.size = 0
  def push(self, node):
    print("We are pushing:", node.user, "\n")
    node.next = self.head
    self.head = node
    self.size += 1

  def pop(self):
    if self.size == 0:
      print("Cannot pop from an empty stack! Push first...\n")
    else:
      print("We are removing:", self.head.user)
      current = self.head
      self.head = self.head.next
      current.next = None
      self.size -= 1
  
  def peek(self):
    if self.size == 0:
      print("Cannot peek from an empty stack! Push first...\n")
    else:
      print("\nThe top node has the value of:", self.head.user, "\n")

  def isEmpty(self):
    return self.size == 0