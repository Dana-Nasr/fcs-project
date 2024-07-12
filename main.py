from socialPlatform import Graph
from user import User
from node import Node
from stack import Stack
from queu import Queue
  
def main():
    
    graph = Graph()
    
    user1 = User(1, "sara", ['math', 'Science'], {'interested_in_topics': ['geometry']})
    user2 = User(2, "lana", ['history', 'math'], {'interested_in_topics': ['acient eygpt']})
    user3 = User(3, "heba", ['math', 'art'], {'interested_in_topics': ['geometry']})
    user4 = User(4, "dani", ['science', 'english'], {'interested_in_topics': []})
    
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