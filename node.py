class Node:
    def __init__(self, user, weight=1, next=None):
        self.user = user                # User object
        self.weight = weight            # Weight associated with the node
        self.next = next                # Reference to the next node in the linked list