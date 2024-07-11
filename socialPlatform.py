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

class Graph:                #the graph probably is spare that's why an adjacency list is used
  def __init__(self):
    self.adj_list = {}

  def addVertex(self, vertex):
    if vertex not in self.adj_list:
      self.adj_list[vertex] = LinkedList()      #add a node to the linked list
      print("Vertex", vertex, "has been added!\n")
      return
    print("Vertex", vertex, "already exists!\n")
  