
# LINKED LIST EXAMPLE
"""
Return the nth from the last element of the list

For example:
If the values of the list are: 
[12, 35, 47, 3, 23, 51, 97]

and your are required to return the 3rd element from the last element of the list
The expected return value should be 23
"""

from linkedList import LinkedList


ll = LinkedList()

n =  3

value_list = [12, 35, 47, 3, 23, 51, 97]

def return_nth(n):
    for i in value_list:
        ll.append(i)

    # Create two pointers to the head of the list
    first_pointer = ll.head
    second_pointer = ll.head

    # Set the two pointers n elements apart.
    # This is achieved by moving the first pointer n elements forward.
    for i in range(n):
        if first_pointer == None:
            return None
        first_pointer = first_pointer.next

    # Iterate the list checking the first pointer with the while loop and moving both pointers forward 
    # inside the loop.
    # When the first pointer reaches the end of the list, the second pointer will be pointing to the nth element
    # to the end of the list
    while first_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    # 5. Return the the value of the first pointer (which is the nth to the last element).
    return second_pointer.value

print(return_nth(3))
    

    
