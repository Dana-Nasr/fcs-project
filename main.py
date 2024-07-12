from socialPlatform import Graph
from user import User
from node import Node

  
def main():
    user1 = User(1, "Hani", ["Math", "Science"], {"interested_in_topics": ["Physics"], "already_known_topics": ["Algebra"]})
    user2 = User(2, "Salam", ["History"], {"interested_in_topics": ["Math"], "already_known_topics": ["Ancient History"]})
    user3 = User(3, "Fadi", ["Computer Science", "Physics"], {"interested_in_topics": ["Algebra"], "already_known_topics": ["Gravity"]})
    

    #  node1=Node(user1,0)
    #  node2=Node(user2,0)
    #  node3=Node(user3,0)


    graph = Graph()
    graph.addVertex(user1)
    graph.addVertex(user2)
    graph.addVertex(user3)

    graph.displayGraph()
main()