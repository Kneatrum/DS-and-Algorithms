
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
        if self.length > 1:
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

        
    # Adding a node to the doubly linked list
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
            self.length += 1

    
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
            
    
    # Removing the first node from the list
    def pop_first(self):
        # If the linked list is empty, return none.
        if self.head == None:
            return None
        # If the length of the list is 1, delete it from the list
        to_pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return to_pop
        # Else, set the second node as the head of the list and delete the first node.
        else:
            self.head = to_pop.next
            self.head.prev = None
            to_pop.next = None
            self.length -= 1
            return to_pop
    

    # Removing the last node from the list
    def pop_last(self):
        # If the list is empty, return None
        if self.length == 0:
            return False
        # If the length of the list is 1, delete it from the list
        to_pop = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return to_pop
        # Else, set the second last node as the tail and delete the last node.
        else:
            self.tail = to_pop.prev
            self.tail.next = None
            to_pop.prev = None
            to_pop.next = None
            self.length -= 1
            return to_pop
    

    # Getting a node from a specific position in the doubly linked list.
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.head is None or self.length == 0:
            return None
        # If the index  is less than half of the length, start from the beginning.
        if index < self.length // 2:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
        # Else, start from the tail if the index is more than half of the length of the linked list.
        else:
            temp_node = self.tail
            for _ in range(self.length - 1, index, -1):
                temp_node = temp_node.prev
        return temp_node
    

    # Setting the value of a node from a specific position in the doubly linked list.
    def set(self, index, value):
        node =  self.get(index)
        if node is not None:
            node.value = value
            return True
        return False


    # Deleting a node from a specific position in the doubly linked list.
    def delete(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop_last()
        else:
            to_delete = self.get(index)
            to_delete.prev.next = to_delete.next
            to_delete.next.prev = to_delete.prev
            to_delete.next = None
            to_delete.prev = None
            self.length -= 1
            return to_delete


    # Searching a node in the doubly linked list
    def search(self, target):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.value == target:
                return True
            temp_node = temp_node.next
        return False
    

    # Insert method
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print("Index out of range")
            return 
        elif index == 0:
            self.prepend(value)
            return
        else:
            new_node = Node(value)
            node =  self.get(index - 1)
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node
            self.length += 1
        

        



