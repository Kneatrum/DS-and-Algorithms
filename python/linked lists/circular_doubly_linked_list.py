
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
            yield temp_node.value
            temp_node = temp_node.next
            if temp_node == self.head:
                break


    # Creating a linked list.
    def create_cdll(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node


    # Inserting a new node into the cdll.
    def insert_cdll(self, value, index):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            new_node = Node(value)
            if index == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif index == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                temp_index = 0
                while temp_index < index - 1:
                    temp_node = temp_node.next
                    temp_index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            return "Node has been inserted"


    # Traversal method.
    def traverse(self):
        if self.head is None:
            return "List is empty"
        else:
            temp_node = self.head
            while temp_node is not None:
                print(temp_node.value, end=" ")
                if temp_node is self.tail:
                    break
                temp_node = temp_node.next

    
    # Reverse traversal.
    def reverse_traversal(self):
        if self.head is None:
            return "List is empty"
        else:
            temp_node = self.tail
            while temp_node is not None:
                print(temp_node.value, end=" ")
                if temp_node is self.head:
                    break
                temp_node = temp_node.prev
