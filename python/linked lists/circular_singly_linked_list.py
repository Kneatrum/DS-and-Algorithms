
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

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " -> "
        return result


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
            self.tail = new_node
        self.length += 1


    def prepend(self, value):
        new_node = Node(value)
        # If the linked list is empty, create a new node and let the tail point to itself.
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        # Else let the tail point to the new head, and the new node point to the existing head, then set the new node as the new head.
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1
        


