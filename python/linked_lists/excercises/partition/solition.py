# LINKED LIST EXAMPLE

"""
Write a code to partition a linked list around a value X such that 
all nodes less than X come before all nodes greater than or equal to X
"""
from linkedList import LinkedList

linkd_list = LinkedList()

values_list = [3,5,2,56,86,23,93,27,5,76,23,6,67,51]

def partition(linked_list, X):
    current_node = linked_list.head
    linked_list.tail = linked_list.head

    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < X:
            current_node.next = linked_list.head
            linked_list.head = current_node
        else:
            linked_list.tail.next = current_node
            linked_list.tail = current_node
        current_node = next_node

    if linked_list.tail.next is not None:
        linked_list.tail.next = None

    
for i in values_list:
    linkd_list.append(i)

print(linkd_list)
partition(linkd_list, 30)
print(linkd_list)