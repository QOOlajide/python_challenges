def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # 1. Base Case: Both are None (we safely reached the bottom together)
    if not p and not q:
        return True
    
    # 2. Structural/Value Mismatch: One is None OR values are different
    if not p or not q or p.val != q.val:
        return False
    
    # 3. Recurse: Check BOTH the left branches AND the right branches
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
