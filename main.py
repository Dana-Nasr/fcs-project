from socialPlatform import Graph
from user import User
from node import Node
from stack import Stack
from queu import Queue
  
def main():
    
    graph = Graph()
    
    user1 = User(1, "sara", ['math', 'Science'], {'interested_in_topics': ['geometry','algebra']})
    user2 = User(2, "lana", ['history', 'math'], {'interested_in_topics': ['acient eygpt']})
    user3 = User(3, "heba", ['math', 'art'], {'interested_in_topics': ['geometry']})
    user4 = User(4, "dani", ['science', 'english'], {'interested_in_topics': []})
    

    user1.addSubject('arabic')
    user1.addKnownTopic('philosophy')
    user1.changeName('hanadi')
    user1.deleteInterestedTopic('algebra')
    print(user1.getSubjects())
    user1.addInterestedTopic('trigonometry')
    print("user1 after adding subject,intrested topic,changing name and deleting intrested topic")
    user1.printUser()
    print(f"Subjects that user 1 like {user1.getSubjects()}")
    graph.addUser(user1)
    graph.addUser(user2)
    graph.addUser(user3)
    graph.addUser(user4)

    graph.addFriendEdge(1, 2, 4)
    graph.addFriendEdge(1, 3, 2)
    graph.addFriendEdge(2, 4, 1)

    graph.displayGraph()

    graph.recommendFriends(1)

    print("DFS Traversal from sara:")
    graph.dfs(1)
main()