from node import Node
from stack import Stack
from queu import Queue
from user import User  # Ensure User class is imported

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, node):
        new_node = node
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def removeNode(self, user_id):
        temp = self.head
        prev = None
        while temp:
            if temp.user.id == user_id:
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
            print(temp.user.id, end=" -> ")
            temp = temp.next
        print("None")

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.users = {}  # Store user information keyed by user_id

    def addUser(self, user):
        if user.id in self.adj_list:
            print(f"User with ID {user.id} already exists in the graph!\n")
            return
        
        new_node = Node(user)
        self.adj_list[user.id] = LinkedList()
        self.adj_list[user.id].addNode(new_node)
        self.users[user.id] = user
        
        print(f"User {user.name} with ID {user.id} has been added to the graph!\n")

    def addFriendEdge(self, user1_id, user2_id, weight):
        if user1_id in self.adj_list and user2_id in self.adj_list:
            node1 = Node(self.users[user1_id], weight)
            node2 = Node(self.users[user2_id], weight)
            self.adj_list[user1_id].addNode(node2)
            self.adj_list[user2_id].addNode(node1)
            print(f"{self.users[user1_id].name} and {self.users[user2_id].name} are now freinds")
        else:
            print(f"Invalid user IDs {user1_id} and {user2_id}!\n")

    def addFollowEdge(self, user1_id, user2_id, weight=0):
        if user1_id in self.adj_list and user2_id in self.adj_list:
            node = Node(self.users[user2_id], weight)
            self.adj_list[user1_id].addNode(node)
            print(f"{self.users[user1_id].name} is following {self.users[user2_id].name}")
        else:
            print(f"Invalid user IDs {user1_id} and {user2_id}!\n")

    def deleteUser(self, user_id):
        if user_id not in self.adj_list:
            print(f"User ID {user_id} does not exist!\n")
            return
        del self.adj_list[user_id]
        for v in self.adj_list:
            self.adj_list[v].removeNode(user_id)
        print(f"User ID {user_id} has been deleted!\n")

    def displayGraph(self):
        if not self.adj_list:
            print("Graph is empty!\n")
            return
        for user_id in self.adj_list:
            print(f"{user_id}:", end=" ")
            self.adj_list[user_id].displayNodes()
        print()

    def dfs(self, start_user_id):
        if start_user_id not in self.adj_list:
            print(f"Start user ID {start_user_id} not found in the graph")
            return
        
        visited = set()
        stack = Stack()
        stack.push(Node(self.users[start_user_id]))
        
        while not stack.isEmpty():
            vertex_node = stack.pop()
            vertex = vertex_node.user.id
            if vertex not in visited:
                print("Visited:", vertex)
                visited.add(vertex)
                current = self.adj_list[vertex].head
                while current:
                    if current.user.id not in visited:
                        stack.push(Node(current.user))
                    current = current.next

    def bfs(self, start_user_id):
        if start_user_id not in self.adj_list:
            print(f"Start user ID {start_user_id} not found in the graph")
            return
        
        visited = set()
        queue = Queue()
        queue.inqueue(Node(self.users[start_user_id]))
        
        while queue.head is not None:
            vertex_node = queue.dequeue()
            vertex = vertex_node.user.id
            if vertex not in visited:
                print("Visited:", vertex)
                visited.add(vertex)
                current = self.adj_list[vertex].head
                while current:
                    if current.user.id not in visited:
                        queue.inqueue(Node(current.user))
                    current = current.next

    def checkFriendship(self, vertex1, vertex2):
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            print(f"One or both users do not exist in the graph!\n")
            return

        current = self.adj_list[vertex1].head
        while current:
            if current.user.id == vertex2:
                weight = current.weight
                if weight <= 2:
                    print(f"{self.users[vertex1].name} and {self.users[vertex2].name} are not close friends. degree of freindship: {weight}")
                else:
                    print(f"{self.users[vertex1].name} and {self.users[vertex2].name} are close friends. degree of freindship: {weight}")
                return
            current = current.next

        print(f"{self.users[vertex1].name} and {self.users[vertex2].name} are not friends.\n")
    
       
    def checkFollwers(self, vertex1, vertex2):
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list:
            print(f"One or both users do not exist in the graph!\n")
            return

        current = self.adj_list[vertex1].head
        while current:
            if current.user.id == vertex2:
                weight = current.weight
                if weight == 0:
                    print(f"{self.users[vertex1].name} follows {self.users[vertex2].name} \n")
                    return     
             
            current = current.next
        print(f"{self.users[vertex1].name} do not follow {self.users[vertex2].name} \n")
    def recommendFriends(self, user_id,name):
        if user_id not in self.users:
            print(f"User ID {user_id} does not exist!\n")
            return

        user_subjects = set(self.users[user_id].subjects)
        user_topics = set(self.users[user_id].topics.get('interested_in_topics', []))

        recommendations = []

        for other_user_id, other_user in self.users.items():
            if other_user_id == user_id:
                continue

            other_user_subjects = set(other_user.subjects)
            other_user_topics = set(other_user.topics.get('interested_in_topics', []))

            common_subjects = user_subjects.intersection(other_user_subjects)   #finding comom elements
            common_topics = user_topics.intersection(other_user_topics)

            common_interests_count = len(common_subjects) + len(common_topics)

            if common_interests_count > 0:
                recommendations.append((common_interests_count, other_user_id))

       

        print(f"Friend recommendations for user {name}:")
        for count, friend_id in recommendations:
            print(f"User ID: {friend_id}, Name: {self.users[friend_id].name}, Common Interests: {count}")


