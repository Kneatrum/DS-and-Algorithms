
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    # A method to print the linked list
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value) 
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    

    # Implementation of the method to append a new node to the linked list.
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    #implementation of the method to prepend a new node to the linked list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    # Implementation of a method to add a new node to a specific index in the linked list.
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        # Prevent insertion to a negative index or an index greater than the length of the linked list
        if index < 0 or index >= self.length:
            return False
        # If the linked list is empty, set the new node as the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If it is the 0th index, we need to set the new node as the head.
        elif index == 0:
            new_node.next = temp_node
            self.head = new_node
        # Else, loop to (index - 1), set the new node's next pointer
        # to the temp node's next pointer (index), and then set the current node (temp_node's) next pointer to the new node
        else: 
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1


    # Traversing a linked list.
    def traverse(self):
        current = self.head
        while current is not None:
            if current.next is not None:
                print(current.value, end=' ') # Adding a space after printing the value if the next value is not null.
            else:
                print(current.value)
            current = current.next


    # Searching for a node in a linked list.
    def search(self, node):
        current = self.head
        while current is not None:
            if current.value == node:
                return True
            current = current.next
        return False
    

    # Get value form a specific index in a linked list
    def get(self, index):
        # Return none if the index is less than -1 or greater than the length of the linked list.
        if index >= self.length or index < -1:
            return None
        # Return the last element
        if index == -1:
            return self.tail
        # Get the head and loop to the desired index then return its value
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    

    # Update value form a specific index in a linked list
    def update(self, index, new_value):
        # Return False if the index is less than -1 or greater than the length of the linked list.
        if index >= self.length or index < -1:
            return False
        # Update the value of the last element.
        if index == -1:
            self.tail.value = new_value
        # Get the head and loop to the desired index then update its value
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = new_value


    # Delete the first element from the linked list
    def pop_first(self):
        # In case the length of the linked list is 0, return none.
        if self.length == 0:
            return None
        to_pop = self.head
        # In case the length of the linked list is 1, just set the head and tail to None.
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        # Set the first node's next pointer to none
        # Set the next pointer of the first node to the new head.
        else:
            self.head = to_pop.next
            to_pop.next = None
            self.length -= 1
        return to_pop
    

    # Delete the last node from the linked list.
    def pop(self):
        last_element = self.tail
        # If the linked list is empty, return None.
        if self.length == 0:
            return None
        # If the length of the linked list is 1, remove it by settin the head and tail pointer to None.
        if self.length == 1:
            self.head = self.tail = None
        else:    
            temp = self.head
            while temp.next is not last_element: # Loop to the second last element of the linked list
                temp = temp.next
            self.tail = temp # Set the tail to the second last element of the linked list
            temp.next = None # Set the next pointer to None.
            self.length -= 1 # Reduce the length of the linked list by 1
            return last_element # Return the the last element of the initial linked list.
        

    # Delete a node from a specific index in the linked list
    def delete(self, index):
        # First method.
        # If the index is more then the length of the linked list or less than -1, return None
        if index >= self.length or index <- 1:
            return None
        # If the index is 0, that means we can only pop the first element.
        if index == 0:
            return self.pop_first()
        # If the index points to the last elemen, it means we can only remove the last element (pop).
        if index == self.length - 1 or index == -1:
            return self.pop()     
        prev_node = self.get(index - 1)
        to_delete = prev_node.next
        prev_node.next = to_delete.next
        to_delete.next = None
        self.length -= 1
        
        # Second method. (Just for fun:)
        '''
        current = self.head
        before = None
        to_delete = None
        for i in range(index + 1):
            if i == index - 1:
                before = current
            elif i == index:
                to_delete = current
            current = current.next
        before.next = current
        to_delete.next = None
        self.length -= 1
        '''

        return to_delete
    

    # Delete entire linked list.
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


    # Reverse a singly linked list
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node


    # Find the middle of a linked list.
    def find_middle(self):
        current = self.head
        mid =  int(self.length/2)
        if self.length % 2 == 0:
            for _ in range(mid):
                current = current.next
            return current.value
        else:
            for _ in range(round(mid)):
                current = current.next
            return current.value
    '''
    # Tortoise and hare algorithm
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    '''    


    # Removing duplicates from a linked list
    def remove_duplicates(self):
        seen = set()
        prev = None
        current = self.head
        while current is not None:
            if current.value in seen:
                # Remove the current node
                prev.next = current.next
            else:
                # Add the current value to the set
                seen.add(current.value)
                prev = current
            current = current.next




