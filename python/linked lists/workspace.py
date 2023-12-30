from singly_linked_list import *
from circular_singly_linked_list import *
from doubly_linked_list import *
from circular_doubly_linked_list import *





cdll = CircularDoublyLinkedList()


cdll.create_cdll(5)
print([temp_node.value for temp_node in cdll]) 
























"""
dl_list = DoublyLinkedList()


# Appending nodes to a doubly linked list
dl_list.append(10)
dl_list.append(20)
dl_list.append(30)


# Printing the last and previous values of the node.
print(dl_list.tail.value)
print(dl_list.tail.prev.value)



print(dl_list)


# Prependig a  node to the doubly linked list
dl_list.prepend(5)
print(dl_list)


# Traversing the list forwards and backwards.
dl_list.traverse_backward()
dl_list.traverse_forward()


# # Removing the the first node from the list
# dl_list.pop_first()
# print(dl_list)

# # Removing the last node from the list
# dl_list.pop_last()
# print(dl_list)


# Getting a node from a specific index in the doubly linked list
print(dl_list.length)
print(dl_list)
# print(dl_list.get(1).value)
print(dl_list.get(1).value)


# Searching for a  value in the list.
print(dl_list.search(10))
print(dl_list.length)


# Setting a value in a specific node.
print(dl_list.set(0, 10))
print(dl_list)



# Deleting a node from any position in the list.
dl_list.delete(3)
print(dl_list)



# Inserting a node to any position in the list.
print(dl_list.insert(2, 100))
print(dl_list)
"""

























"""

# Create an instance of a circular_singly_linked_list
c_linked_list = CircularSinglyLinkedList()


# Append a new value to the list and print it out
c_linked_list.append(10)
c_linked_list.append(20)
c_linked_list.append(30)
print(c_linked_list)


# Prepend a new value to the list and print it out
c_linked_list.prepend(5)
print(c_linked_list)


# Insert a new value to any position in the list
c_linked_list.insert(40, 2)
print(c_linked_list)


# Traversing a circular_singly_linked_list
c_linked_list.traverse()


# Searching for an element in the list
element = c_linked_list.search(10)
if element is not None:
    print("Found element")
else:
    print("No element found")


# Retrieving a value from a specific index in the list
print(c_linked_list.get(0).value)


# Updating a value from a specific index in the list
c_linked_list.set(0, 100)
print(c_linked_list)


# Removing the first element from the list
c_linked_list.pop_first()
print(c_linked_list)


# Removing an element from any position in the list
c_linked_list.remove(0)
print(c_linked_list)


c_linked_list.delete_all()
print(c_linked_list)

"""



























# new_linked_list = SinglyLinkedList()

# new_linked_list.append(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# new_linked_list.append(50)

# print(new_linked_list)
# print("Length of linked list: " + str(new_linked_list.length))

# new_linked_list.prepend(5)
# print(new_linked_list)
# print("Length of linked list: " + str(new_linked_list.length))

# new_linked_list.insert(2, 15)
# print(new_linked_list)
# print("Length of linked list: " + str(new_linked_list.length))

# new_linked_list.traverse()

# if (new_linked_list.search(2)):
#     print("Found")
# else:
#     print("Not found")

# result = new_linked_list.get(0)
# if (result):
#     print(result)
# else:
#     print("No element found in that index")

# new_linked_list.update(2, 5)
# print(new_linked_list)

# new_linked_list.pop_first()
# print(new_linked_list)


# new_linked_list.delete(-1)
# print(new_linked_list)

# # new_linked_list.delete_all()
# # print(new_linked_list)

# new_linked_list.reverse()
# print(new_linked_list)

