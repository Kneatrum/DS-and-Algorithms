
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


    # Search method.
    def search(self, value):
        if self.head is None:
            return "List is empty"
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    return temp_node.value
                if temp_node == self.tail:
                    return "Value not found"
                temp_node = temp_node.next
            return None
        

    # Delete a node from the circular doubly linked list
    def delete_node(self, location):
        if self.head == None:
            print("List is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next =  self.head
                    self.head.prev = self.tail
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.prev = current_node
            print("Node deleted")

    # Delete entire CDLL
    def delete_all(self):
        if self.head == None:
            return "List is already empty"
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            return "List has been deleted"


