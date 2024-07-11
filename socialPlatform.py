class LinkedList:

   def __init__(self):
    self.head = None
    self.size = 0
  
   def addNode(self, data,weight):
    new_node = Node(data,weight)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

   def displayNodes(self):
    temp = self.head
    while temp:
      print(temp.data, end=" -> ")
      temp = temp.next
    print("None")

class Graph:
  