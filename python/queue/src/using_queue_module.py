
"""
Using the queue module to implement a FIFO queue.
"""

import queue as q

my_queue = q.Queue(maxsize=3)

# Check if the queue is empty
print(my_queue.empty())

# Check if the queue is full
print(my_queue.full())

# Check the size of the queue
print(my_queue.qsize())

# Adding elements to the queue
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)


# Check if the queue is empty
print(my_queue.empty())


# Check if the queue is full
print(my_queue.full())


# Check the size of the queue
print(my_queue.qsize())
print(my_queue)


# Remove  the first element from the queue or dequeue.
print(my_queue.get())

