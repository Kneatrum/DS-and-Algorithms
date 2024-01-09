 
class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def add_child(self, TreeNode):
        self.children.append(TreeNode)


# The root node
tree = TreeNode('Drinks', [])

# Creating two children to the root node
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])

# Adding the two children to the root node
tree.add_child(cold)
tree.add_child(hot)

# Creating two children for the cold node
fanta = TreeNode('Fanta', [])
cola = TreeNode('Cola', [])

# Creating two children for the hot node
coffee = TreeNode('Coffee', [])
tea = TreeNode('Tea', [])

# Adding children to the cold node
cold.add_child(fanta)
cold.add_child(cola)

# Adding childred to the hot node
hot.add_child(coffee)
hot.add_child(tea)

# Print the entire tree
print(tree)

        