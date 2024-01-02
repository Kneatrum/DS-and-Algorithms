
"""
Removing duplicates from the list below.
1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5

Expected result is
1 -> 2 -> 3 -> 4 -> 5

"""

from linkedList import LinkedList

ll = LinkedList()

def remove_duplicates(ll):
    current = ll.head
    my_set = set()
    prev = None
    while current:
        if current.value not in my_set:
            my_set.add(current.value)
            prev = current
        else:
            prev.next = current.next
        current = current.next

        

value_list = [1, 2, 2, 3, 4, 4, 4, 5]

# Appending the values into the linked list
for i in value_list:
    ll.append(i)

# Printing the list with duplicates
print(ll)

# Removing duplicates
remove_duplicates(ll)

# Printing the list without duplicates
print(ll)