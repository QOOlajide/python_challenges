#Understand: Creating a binary tree with different pointers. It’d be illogical to define the root first and assign it to left and right variables I haven’t defined yet.

#1. Create the node with value 4 (left child)
#2. Create the node with value 6 (right child)
#3. Create the node with value 10 and assign left=4 and right=6



class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Step 1: Create the left child
left_child = TreeNode(4)

# Step 2: Create the right child
right_child = TreeNode(6)

# Step 3: Create the root node and assign the left and right children
root = TreeNode(10, left_child, right_child)
