
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def pop_first(self):
        if self.length == 0  or self.head == None:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            to_delete =  self.head
            self.head = self.head.next
            to_delete.next = None
            
    def pop(self):
        if self.length == 0 or self.head == None:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            to_delete =  temp_node.next
            temp_node.next =  to_delete.next
            to_delete.next = None
            self.length -= 1