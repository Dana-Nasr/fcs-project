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

  def addFreindEdge(self, vertex1, vertex2,weight):
    if vertex1 in self.adj_list and vertex2 in self.adj_list:    #undirected to serve as friends weight determine how much they are friends
      self.adj_list[vertex1].addNode(vertex2,weight)
      self.adj_list[vertex2].addNode(vertex1,weight)
    elif vertex1 not in self.adj_list and vertex2 not in self.adj_list:
      print("Invalid vertices", vertex1, "and", vertex2, "\n")
    elif vertex1 not in self.adj_list:
      print("Invalid vertex", vertex1, "\n")
    else:
      print("Invalid vertex", vertex2, "\n")
  
  def addfollowEdge(self, vertex1, vertex2,weight=0):
    if vertex1 in self.adj_list and vertex2 in self.adj_list:    #directed to serve as follow weight=0 
      self.adj_list[vertex1].addNode(vertex2,weight)

    elif vertex1 not in self.adj_list and vertex2 not in self.adj_list:
      print("Invalid vertices", vertex1, "and", vertex2, "\n")
    elif vertex1 not in self.adj_list:
      print("Invalid vertex", vertex1, "\n")
    else:
      print("Invalid vertex", vertex2, "\n")

  def displayGraph(self):
    if self.adj_list == {}:
      print("Graph is empty!\n")
      return
    for vertex in self.adj_list:
      print(vertex + ":", end=" ")
      self.adj_list[vertex].displayNodes()
    print()