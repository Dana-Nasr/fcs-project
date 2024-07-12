from socialPlatform import Graph
from user import User
from node import Node
from stack import Stack
from queu import Queue
  
def main():
    # Initialize a graph
    graph = Graph()
    
    # Add users
    graph.addUser(1, "Alice", subjects=['Math', 'Science'], topics={})
    graph.addUser(2, "Bob", subjects=['History', 'Art'], topics={})
    graph.addUser(3, "Charlie", subjects=['Math', 'Art'], topics={})
    graph.addUser(4, "Diana Smith", subjects=['Science', 'History'], topics={})
    
    # Display the initial graph
    print("Initial Graph:")
    graph.displayGraph()
    
    # Add relationships (edges)
    graph.addFriendEdge(1, 2,4)
    graph.addFriendEdge(2, 4,7)
    graph.addFollowEdge(1, 3,5)
    
    # Display the updated graph
    print("Updated Graph with Relationships:")
    graph.displayGraph()
    
    # Perform DFS from Alice (vertex 1)
    print("DFS Traversal from Alice (vertex 1):")
    graph.dfs(1)
    
    # Perform BFS from Alice (vertex 1)
    print("BFS Traversal from Alice (vertex 1):")
    graph.bfs(1)

main()
