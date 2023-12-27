from singly_linked_list import *
from circular_singly_linked_list import *









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

