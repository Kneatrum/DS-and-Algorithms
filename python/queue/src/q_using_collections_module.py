

"""
Using the collections module to implement a FIFO queue.
"""

from collections import deque

my_queue = deque(maxlen = 3)

my_queue.append(1)
my_queue.append(2)
my_queue.append(3)

# The first element will be overwritten by this new element in the append method below. Because the queue is full
# my_queue.append(4)

print(my_queue)

# This removes the first element from the queue
print("Removed ", my_queue.popleft())
print("Resilt ", my_queue)

my_queue.clear()
print("Deleted queue ", my_queue)
