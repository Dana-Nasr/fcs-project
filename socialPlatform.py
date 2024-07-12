from node import Node
from stack import Stack
from queu import Queue

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, node):
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

class Graph:
    def __init__(self):
        self.adj_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = LinkedList()  
            print(f"Vertex {vertex} has been added!\n")
        else:
            print(f"Vertex {vertex} already exists!\n")

    def addUser(self, user_id, name, subjects=None, topics=None):
        if user_id in self.adj_list:
            print(f"User with ID {user_id} already exists in the graph!\n")
            return
        
        new_node = Node(user_id, name)  # creating a user
        if subjects:
            new_node.subjects = subjects
        if topics:
            new_node.topics = topics
      
        self.adj_list[user_id] = LinkedList()
        self.adj_list[user_id].addNode(new_node)
        
        print(f"User {name} with ID {user_id} has been added to the graph!\n")

    def addFriendEdge(self, vertex1, vertex2, weight):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            node1 = Node(vertex1, weight)
            node2 = Node(vertex2, weight)
            self.adj_list[vertex1].addNode(node2)          # not directed to show they are friends
            self.adj_list[vertex2].addNode(node1)
        else:
            print(f"Invalid vertices {vertex1} and {vertex2}!\n")

    def addFollowEdge(self, vertex1, vertex2, weight=0):                #directed indicates follow
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            node = Node(vertex2, weight)
            self.adj_list[vertex1].addNode(node)          
            
        else:
            print(f"Invalid vertices {vertex1} and {vertex2}!\n")

    def deleteVertex(self, vertex):
        if vertex not in self.adj_list:
            print(f"Vertex {vertex} does not exist!\n")
            return
        del self.adj_list[vertex]
        for v in self.adj_list:
            self.adj_list[v].removeNode(vertex)
        print(f"Vertex {vertex} has been deleted!\n")

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
        
        visited = set()
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
                        stack.push(Node(current.user, 0))  #push the adj 
                    current = current.next

    def bfs(self, start_vertex):
        if start_vertex not in self.adj_list:
            print(f"Start vertex {start_vertex} not found in the graph")
            return
        
        visited = set()
        queue = Queue()
        queue.inqueue(start_vertex)  
        
        while queue.head is not None:
            vertex = queue.dequeue()
            if vertex not in visited:
                print("Visited:", vertex)
                visited.add(vertex)
                current = self.adj_list[vertex].head
                while current:
                    if current.user not in visited:
                        queue.inqueue(current.user)  # inqueue adj
                    current = current.next