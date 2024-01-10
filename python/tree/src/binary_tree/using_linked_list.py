"""
Using a linked list to create a binary tree.

"""

import queue_linkedlist as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None



def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        my_queue = queue.Queue()
        my_queue.enqueue(root_node)
        while not my_queue.is_empty():
            root = my_queue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                my_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                my_queue.enqueue(root.value.right_child)


def search_binary_tree(root_node, node_value):
    if not root_node:
        return "The binary tree does not exist"
    else:
        my_queue = queue.Queue()
        my_queue.enqueue(root_node)
        while not my_queue.is_empty():
            root = my_queue.dequeue()
            if root.value.data == node_value:
                return "Success"
            if root.value.left_child is not None:
                my_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                my_queue.enqueue(root.value.right_child)
        return "Not found"




# Instance of the binary tree
binary_tree = TreeNode("Drinks")

# Creating the left and right child nodes
left_child = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
left_child.left_child = tea
left_child.right_child = coffee
right_child = TreeNode("Cold")

binary_tree.left_child = left_child
binary_tree.right_child = right_child


"""
           TRAVERSAL OF THE BINARY TREE
_________________________________________________________
"""

# Traversing the binary tree using the In Order Traversal
# in_order_traversal(binary_tree)

# Traversing the binary tree using the pre order traversal
# pre_order_traversal(binary_tree)

# Traversing the binary tree using the post order traversal
# post_order_traversal(binary_tree)

# Slevel_order_traversal(binary_tree)

print(search_binary_tree(binary_tree, "Tea"))


