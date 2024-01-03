"""
Implementing a stack using python lists with a limited number of items.
"""

class Stack(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []


    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    

    # Check if the stack is empty
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
        

    # Check if the stack is full
    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False
        
    
    # Add a new item to the stack
    def push(self,value):
        if not self.is_full():
            self.list.append(value)
            return "The element has been added to the stack"
        else:
            return "Sorry: The stack is full"
        
    
    # Remove the last or top value from the stack
    def pop(self):
        if not self.is_empty():
            self.list.pop()
            return "The element has been removed from the stack"    
        else:
            return "The stack is empty"
        
    
    # Return the last element from the stack
    def peek(self):
        if not self.is_empty():
            return self.list[len(self.list) - 1]
        else:
            return "The stack is empty"
        

    # Delete the entire stack
    def delete(self):
        self.list = None
        