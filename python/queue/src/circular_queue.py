

class Queue:
    # Initializing a queue
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.top = -1
        self.start = -1


    # Helper function to print the queue
    def __str__(self):
        values = ''
        values = [str(x) for x in self.items]
        return ' '.join(values)
    

    # Checking if queue is full.
    def isFull(self):
        # If start is 0 and top is max size, or if top + 1 is self.start, the queue is full.
        if self.start == 0 and self.top + 1 ==  self.max_size or self.top + 1 == self.start:
            return True
        else: return False
        

    # Checking if queue is empty.
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    
    # Adding an element to the queue
    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top == -1:
                self.top = 0
                self.start = 0
                self.items[self.top] = value
            else:
                # If we are here, the queue is not full.
                # But the top element points to the last element of the queue.
                # This means that there is space at the beginning of the queue
                # Or the start element doesn't point to the first position.
                # So, lets move the top element to the start of the queue.
                if self.top + 1 == self.max_size:
                    self.top = 0
                else:
                    self.top += 1
                    # In the enqueue method, we only move the start element if it was initially -1
                    # Otherwise, it will be moved in the dequeue method
                    if self.start == -1:
                        self.start = 0
                self.items[self.top] = value
                return "Element has been inserted into queue"
            
    
    # Removinf an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            # Store the first element and the start element
            start =  self.start
            first_element = self.items[start]

            # If this is the only element in the queue
            if self.top == self.start:
                self.start = -1
                self.top = -1
            # If the start element points to the last element in the queue
            # Move it to the beginning of the queue
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element
        
    
    # Peek 
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[self.start]
        
    
    # Delete all elements from the queue
    def delete(self):
        self.items = self.max_size * [None]
        self.start = -1
        self.top = -1

            



my_queue = Queue(3)

# Enqueue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue)

print("Empty:", my_queue.isEmpty())
print("Full:", my_queue.isFull())

print("Peek: ", my_queue.peek())

# Dequeue
my_queue.dequeue()
my_queue.dequeue()
print(my_queue)


