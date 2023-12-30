
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    # Iterator 
    def __iter__(self):
        temp_node = self.head
        while temp_node:
            yield temp_node
            node = temp_node.next
            if node == self.tail.next:
                break


    # Creating a linked list.
    def create_cdll(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node




