

class Stack:
    def __init__(self):
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
        
    
    # Inserting an element to the end of the stack
    def push(self, value):
        self.list.append(value)
        return "Element successfully inserted"
    

    # Return the top element of the stack
    def pop(self):
        if self.is_empty():
            return "The stack is empty"
        else:
            return self.list.pop()

    
    # Return the last element of the stack without removing it
    def peek(self):
        if self.is_empty():
            return "The list is empty"
        else:
            # Return the last element of the stack
            return self.list[len(self.list) - 1]
        
    
    # Delete entire list
    def delete(self):
        self.list = None
