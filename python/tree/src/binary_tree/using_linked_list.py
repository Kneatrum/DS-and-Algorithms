"""
Using a linked list to create a binary tree.

"""

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






# Instance of the binary tree
binary_tree = TreeNode("Drinks")

# Creating the left and right child nodes
hot = TreeNode("Hot")
cold = TreeNode("Cold")

# Adding the children to the binary tree
binary_tree.left_child = hot
binary_tree.right_child = cold

"""
           TRAVERSAL OF THE BINARY TREE
_________________________________________________________
"""

# Traversing the binary tree using the In Order Traversal
# in_order_traversal(binary_tree)

# Traversing the binary tree using the pre order traversal
# pre_order_traversal(binary_tree)

# Traversing the binary tree using the post order traversal
post_order_traversal(binary_tree)