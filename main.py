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
    user5 = User(5, "sami", ['science', 'english'], {'interested_in_topics': []})
    user6 = User(6, "hani", ['science', 'english'], {'interested_in_topics': []})
    
    user1.printUser()
    user1.addSubject('arabic')
    print(f"printing:{user1.getName()} after subject is added")
    user1.printUser()
   
    user1.addKnownTopic('philosophy')
    print(f"printing:{user1.getName()} after known topic is added")
    user1.printUser()

 
    user1.changeName('hanadi')
    print(f"printing:{user1.getName()} after name is changed")
    user1.printUser()
    
  
    user1.deleteInterestedTopic('algebra')
    user1.addInterestedTopic('trigonometry')
    print(f"printing:{user1.getName()} after one of the topics she is intrested in is deleted and another is added")
    user1.printUser()

    print(f"Subjects that {user1.getName()} like {user1.getSubjects()}")
    print("\n ******************************************")
    print("**********ADDING USERS TO GRAPH************")
    print("******************************************")
    graph.addUser(user1)
    graph.addUser(user2)
    graph.addUser(user3)
    graph.addUser(user4)
    graph.addUser(user5)
    graph.addUser(user6)
    graph.addUser(user5)
    print("\n **************************************************")
    print("**********ADDING FRIEND AND FOLLOW EDGE***********")
    print("**************************************************")
    
    graph.addFriendEdge(1, 2, 4)
    graph.addFriendEdge(1, 3, 2)
    graph.addFriendEdge(2, 4, 1)
    graph.addFriendEdge(2, 6, 1)
    graph.addFollowEdge(3,2)
    print("\n ******************************************")
    print("**********DISPLAYING GRAPH***********")
    print("******************************************")
    graph.displayGraph()
    graph.deleteUser(5)
    print(f"graph after deleting {user5.getName()}")
    graph.displayGraph()
    graph.deleteUser(7)
    graph.deleteUser(4)
    print(f"graph after deleting {user4.getName()}")
    graph.displayGraph()
    print("\n ******************************************")
    print("**********CHECKING FRIENDSHIP***********")
    print("*********************************************")
    graph.checkFriendship(4,1)
    graph.checkFriendship(2,1)
    print("\n **************************************************************")
    print("**********Finding out if 2 users follow each other***********")
    print("**************************************************************")
    graph.checkFollwers(3,2)
    graph.checkFollwers(2,3)
    print("\n ******************************************")
    print("**********Recomending friends***********")
    print("**********************************************")
    graph.recommendFriends(1,user1.getName())
    print(" ")
    print("DFS Traversal from sara:")
    graph.dfs(1)
    print(" ")
    print("BFS Traversal from heba:")
    graph.bfs(3)
main()