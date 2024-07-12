class Node:
    def __init__(self, user, weight=0):
        self.user = user                # User object
        self.weight = weight            # Weight associated with the node
        self.next = next                # Reference to the next node in the linked list