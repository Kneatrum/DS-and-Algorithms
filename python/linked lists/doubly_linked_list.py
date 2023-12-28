
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    # This method prints the doubly linked list
    def __str__(self):
        temp_node = self.head
        result = ""
        # Add the first null node to the string.
        if self.length > 0:
            result += str(self.head.prev) + " <--> "

        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            # If the next node is not null, add the double direction arrow
            if temp_node:
                result += " <--> "
            # If the next node is null, add the double direction arrow and the last Null.
            else:
                result += " <--> " + str(self.tail.next) + "\n"
        return result

        


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node  
        self.length += 1


    # Prependind a node to the beginning of the doubly linked list
    def prepend(self, value):
        # If the length of the list is 0, just append the new node
        if self.length == 0:
            self.append(value)
        # Else, set the new node as the new head.
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    
    # Traversing the doubly linked list forwards
    def traverse_forward(self):
        temp_node = self.head
        while temp_node:
            print(str(temp_node.value), end=" ")
            temp_node = temp_node.next
            if temp_node == None:
                print()
                return
    

    # Traversing the doubly linked list in the reverse order
    def traverse_backward(self):
        temp_node = self.tail
        while temp_node:
            print(str(temp_node.value), end=" ")
            temp_node = temp_node.prev
            if temp_node == None:
                print()
                return
