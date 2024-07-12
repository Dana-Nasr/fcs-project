from socialPlatform import Graph
from user import User
from node import Node
from stack import Stack
from queu import Queue
  
def main():
    
    graph = Graph()
    
    graph.addUser(1, "sara", subjects=['math', 'science'], topics={})
    graph.addUser(2, "leen", subjects=['history', 'math'], topics={})
    graph.addUser(3, "samer", subjects=['math', 'english'], topics={})
    graph.addUser(4, "hadi", subjects=['science', 'history'], topics={})
    
    print("Initial Graph:")
    graph.displayGraph()
  
     # Adding edges
    graph.addFriendEdge(1, 2, 4)
    graph.addFriendEdge(1, 3, 2)
    graph.addFriendEdge(2, 4, 1)

    # Display graph
    graph.displayGraph()

    # Friend recommendations
    graph.recommendFriends(1)

    # Traversals
    print("DFS Traversal from Alice (vertex 1):")
    graph.dfs(1)
    
    
main()
