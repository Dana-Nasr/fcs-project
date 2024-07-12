from socialPlatform import Graph
from user import User
from node import Node
from stack import Stack
from queu import Queue
  
def main():
    # Create Users
    user1 = User(1, "sara", ["Math", "Science"], {})
    user2 = User(2, "heba", ["History", "Art"], {})
    user3 = User(3, "fadi", ["Math", "Art"], {})
    user4 = User(4, "dalal", ["Science", "History"], {})

    # Print Users
    user1.printUser()
    user2.printUser()
    user3.printUser()
    user4.printUser()

    # Modify Users
    user1.addSubject("Physics")
    user2.addInterestedTopic(" Mechanics")
    user3.addKnownTopic(" Art")
    user4.changeName("david nasr")

    # Print Modified Users
    user1.printUser()
    user2.printUser()
    user3.printUser()
    user4.printUser()

    # Create Graph
    graph = Graph()

    # Add vertices
    graph.addVertex("sara")
    graph.addVertex("heba")
    graph.addVertex("fadi")
    graph.addVertex("david")

    # Add edges
    graph.addFriendEdge("sara", "heba", 5)
    graph.addFriendEdge("fadi", "sara", 3)
    graph.addFollowEdge("david", "sara")

    # Display Graph
    graph.displayGraph()

    # DFS Traversal
    print("DFS Traversal from sara:")
    graph.dfs("sara")

    # BFS Traversal
    print("BFS Traversal from sara:")
    graph.bfs("sara")

    


main()
