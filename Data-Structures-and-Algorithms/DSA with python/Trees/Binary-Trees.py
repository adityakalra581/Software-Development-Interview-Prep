## PREORDER LOGIC:

## LEFT CHILD -- ROOT -- RIGHT CHILD



class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root,find_val)

    def print_tree(self):
        return self.preorder_print(tree.root,"")[:-1]
        ## Here tree is object of the class BinaryTree and [:-1] will print the tree in reverse order.

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left,find_val) or self.preorder_search(start.right,find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
# Should be True.
print(tree.search(5))

# Test print_tree
# Should be 1-2-4-5-3

## PREORDER PRINTING:

## Parent ( 1 ) - 
# 1st left child (2) - 
# left child of 1st child (4) - 
# right child of 1st child (5) - 
# Second right child (3).

# ***************************************

## INPUT TREE:
# ##     1
#       / \
#      2   3
#     / \
#    4   5

## Height = 2

print(tree.print_tree())

### OUTPUT:

# True
# False
# 1-2-4-5-3

### Height of a Binary Tree:

def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1

print("Height of the given tree is:",height(tree.root))

## OUTPUT: Height of the given tree is: 2