

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next



class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()


    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)


    def push(self, value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node


    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            to_delete = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return to_delete


    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            to_delete = self.LinkedList.head.value
            return to_delete
    

    def is_empty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        

    def delete(self):
        self.LinkedList.head = None
        

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
print("_________")
# print(my_stack.pop())
print(my_stack)
print("_________")
print(my_stack.peek())