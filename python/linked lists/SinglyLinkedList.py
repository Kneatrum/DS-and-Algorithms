
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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




new_linked_list = LinkedList()

new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)

print(new_linked_list)
print("Length of linked list: " + str(new_linked_list.length))

new_linked_list.prepend(5)
print(new_linked_list)
print("Length of linked list: " + str(new_linked_list.length))

new_linked_list.insert(2, 15)
print(new_linked_list)
print("Length of linked list: " + str(new_linked_list.length))


