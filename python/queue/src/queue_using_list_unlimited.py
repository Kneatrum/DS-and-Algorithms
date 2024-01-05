

class Queue():
    # Initializing a queue
    def __init__(self):
        self.items = []


    # Helper methiod to print the queue
    def __str__(self):
        values = ""
        values = [str(x) for x in self.items]
        return " ".join(values)
    

    # Checking if the queue is empty
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    

    # Adding a new item to the queue
    def enqueue(self, value):
        # We use the inbuilt function (append) to insert the value
        self.items.append(value)


    # Removing an item from the queue
    def dequeue(self):
        if self.isEmpty():
            return "No element to remove"
        else:
            # We use the inbuilt function (pop(0)) to remove the first element
            return self.items.pop(0)
        
    
    # Returning the first element from the queue without deleting it.
    def peek(self):
        if self.isEmpty():
            return "No element in the queue"
        else:
            return self.items[0]
        
    
    # Deleting a queue
    def delete(self):
        self.items = None



# Creation of an instance 
my_queue = Queue()

# Checking if the queue is empty
print(my_queue.isEmpty())

# Adding elements to the queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue)


# Testing the dequeue method
my_queue.dequeue()
print(my_queue)


# Testing the peek method
print(my_queue.peek())


# Testing the delete method
my_queue.delete()

    
    