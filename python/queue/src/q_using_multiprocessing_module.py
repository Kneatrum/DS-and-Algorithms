"""
Using the Multiprocessing module to implement a FIFO queue.
"""

from multiprocessing import Queue

my_queue = Queue(maxsize=3)

# Adding elements to the queue
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)


# Check the size of the queue
print(my_queue.qsize())


# Removing elements from the queue.
print(my_queue.get())
print(my_queue.get())
print(my_queue.get())

# Check if the queue is full
print("Full: ", my_queue.full())

# Check if the queue is empty
print("Empty: ", my_queue.empty())