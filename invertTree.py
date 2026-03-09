def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    #if not root:
    #    return root
    #Just to check if the root is none so we can know if the tree is empty or something
    #left = invertTree(root.left)
    #since invertTree returns values, might as well assign it to a value. The way the recursion would would is by going all the way to the left
    #right = invertTree(root.right)
    #same thing, but with the right
    #left, right = right, left
    #Hmm, approach might not work because these values get lost. Time to see solution below
    #return root
    #This is needed to create the new tree. Otherwise, the values don't change!
    ###
    # Base case: If the current node (root) is None, just return it. 
    # This case handles empty trees or reaches the end of a branch.
    if not root:
        return root

    # Recursive call on the left child. This will continue until it reaches
    # the leftmost node of the tree or a leaf node.
    invertTree(root.left)

    # Similarly, a recursive call on the right child. It goes down to the 
    # rightmost node or a leaf node.
    invertTree(root.right)

    # After the recursive calls, we swap the left and right children of 
    # the current node. This is the actual "inverting" step where the 
    # left subtree becomes the right subtree and vice versa.
    root.left, root.right = root.right, root.left

    # Return the current node. Initially, this will be the root of the
    # tree, but as the recursion unwinds, it will return intermediate 
    # nodes after inverting their children.
    return root
