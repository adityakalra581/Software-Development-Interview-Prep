class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)


## Insertion is done according the laws of Binary Search trees.(Balanced) 
    
    def insert_helper(self,current,new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right,new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                return self.insert_helper(current.left,new_val)
            else:
                current.left = Node(new_val)

    def insert(self, new_val):
        return self.insert_helper(self.root,new_val)


        
    ## As the tree created is balanced therfore:
    def search_helper(self,current,find_val):
        if current:
            if current.value == find_val:
                return True
            else:
                return self.search_helper(current.left,find_val) or self.search_helper(current.right,find_val)
        return False
        
    def search(self, find_val):
        return self.search_helper(self.root,find_val)


    ## WITHIN CLASS PREORDER PRINTING:
    
    def print_BST(self):
        return self.print_helper(self.root,"")
    
    def print_helper(self,current,ans):
        if current:
            ans += (str(current.value)+"-->")
            ans = self.print_helper(current.left,ans)
            ans = self.print_helper(current.right,ans)
        return ans

## Alternate way:

## Pre-order

## Root --> Left Child --> Right Child.

def preorder(root):
    if root:
        print(root.value,end=" ")
        if root.left:
            preorder(root.left)
        if root.right:
            preorder(root.right)


##In-order:

## Left Child --> Root --> Right Child.

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)






## Post order printing of tree outside the class:

## left child --> right child --> root.

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end=" ")




# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(6)


## TREE STRUCTURE:

                #     4
                #    / \
                #   2   5                        
                #  / \   \
                # 1   3   6

# Check search
# Should be True
print(tree.search(4))

# Should be True
print(tree.search(6))

# Should be False
print(tree.search(10))


## PRINTING TREE IN PREORDER:

print(tree.print_BST())

## 4-->2-->1-->3-->5-->6-->

print("Pre-order traversal of Binary search tree:")
preorder(tree.root)
print()
## 4 2 1 3 5 6


print("In-order traversal of Binary search tree:")
inorder(tree.root)
print()
## 1 2 3 4 5 6

print("Post-order traversal of Binary search tree:")
postorder(tree.root)
## 1 3 2 6 5 4








