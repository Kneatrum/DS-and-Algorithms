

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None

    # def __str__(self):
    #     return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()


    def __str__(self):
        values = ''
        temp_node = self.linkedlist.head
        while temp_node:
            values += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node:
                values += " -> "
        return values
    

    # Check if queue is empty
    def is_empty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
        
    
    # Add an element to the queue.
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    
    # Remove an element from the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            temp =  self.linkedlist.head
            # Checking if we only have one element
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head =  self.linkedlist.head.next
                temp.next = None
            return temp.value # There is an option to remove the .value and enable the __str__ method in the node class for visualization


    # Peek
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.linkedlist.head.value # There is an option to remove the .value and enable the __str__ method in the node class for visualization

  
    # Delete
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None


my_queue = Queue()

# Enqueue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue)


# Dequeue
print(my_queue.dequeue())
print(my_queue)


# Peek
print(my_queue.peek())

# Delete
my_queue.delete()
print(my_queue)


