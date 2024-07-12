from node import Node
from stack import Stack
from queu import Queue

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, data, weight):
        node = Node(data, weight)
        new_node = node
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def removeNode(self, data):
        temp = self.head
        prev = None
        while temp:
            if temp.user == data:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                self.size -= 1
                return True
            prev = temp
            temp = temp.next
        return False

    def displayNodes(self):
        temp = self.head
        while temp:
            print(temp.user, end=" -> ")
            temp = temp.next
        print("None")

class Graph:  # the graph probably is sparse that's why an adjacency list is used
    def __init__(self):
        self.adj_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = LinkedList()  # add a node to the linked list
            print("Vertex", vertex, "has been added!\n")
        else:
            print("Vertex", vertex, "already exists!\n")

    def addFriendEdge(self, vertex1, vertex2, weight):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:  # undirected means friends weight to show how much they are friends
            self.adj_list[vertex1].addNode(vertex2, weight)
            self.adj_list[vertex2].addNode(vertex1, weight)
        else:
            if vertex1 not in self.adj_list:
                print("Invalid vertex", vertex1, "\n")
            if vertex2 not in self.adj_list:
                print("Invalid vertex", vertex2, "\n")

    def addFollowEdge(self, vertex1, vertex2, weight=0):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:  # directed to serve as follow weight=0
            self.adj_list[vertex1].addNode(vertex2, weight)
        else:
            if vertex1 not in self.adj_list:
                print("Invalid vertex", vertex1, "\n")
            if vertex2 not in self.adj_list:
                print("Invalid vertex", vertex2, "\n")

    def deleteVertex(self, vertex):
        if vertex not in self.adj_list:
            print("Vertex", vertex, "does not exist!\n")
            return
        del self.adj_list[vertex]
        for v in self.adj_list:
            self.adj_list[v].removeNode(vertex)  # deletes any connection (edge) to the vertex
        print("Vertex", vertex, "has been deleted!\n")

    def displayGraph(self):
        if not self.adj_list:
            print("Graph is empty!\n")
            return
        for vertex in self.adj_list:
            print(f"{vertex}:", end=" ")
            self.adj_list[vertex].displayNodes()
        print()

    def dfs(self, start_vertex):
        if start_vertex not in self.adj_list:
            print(f"Start vertex {start_vertex} not found in the graph")
            return
        visited = set()  # do not need to be ordered
        stack = Stack()
        stack.push(Node(start_vertex, 0))
        while not stack.isEmpty():
            vertex_node = stack.pop()
            vertex = vertex_node.user
            if vertex not in visited:
                print("Visited:", vertex)
                visited.add(vertex)
                current = self.adj_list[vertex].head
                while current:
                    if current.user not in visited:
                        stack.push(Node(current.user, 0))
                    current = current.next

    def bfs(self, start_vertex):
        if start_vertex not in self.adj_list:
            print(f"Start vertex {start_vertex} not found in the graph")
            return
        visited = set()
        queue = Queue()
        node=Node(start_vertex,0)
        queue.inqueue(node)
        while queue.head is not None:
            vertex_node = queue.dequeue()
            vertex = vertex_node
            if vertex not in visited:
                print("Visited:", vertex)
                visited.add(vertex)
                current = self.adj_list[vertex].head
                while current:
                    if current.user not in visited:
                        queue.inqueue(Node(current.user, 0))
                    current = current.next
