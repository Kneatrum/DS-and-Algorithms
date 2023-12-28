
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