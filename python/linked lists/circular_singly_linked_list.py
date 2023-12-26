
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:

    # Empty circular linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    '''
    # Circular linked list with one node.
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
    '''

    def append(self, value):
        new_node = Node(value)
        # If the linked list is empty, create a new node and let the tail point to itself.
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = new_node
        # If the linked list has one or more nodes, add the newo one and let the tail point to the head.
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        


