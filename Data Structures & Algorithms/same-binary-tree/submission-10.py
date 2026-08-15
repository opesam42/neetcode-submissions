# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root):
        if root is None:
            return None
        
            # return
        if root.left:
            left_root = root.left.val
        else:
            left_root = None
        
        if root.right:
            right_root = root.right.val
        else:
            right_root = None

        return (root.val, left_root, right_root)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # handle empty trees
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False

        print(f"p: {p.val}, q: {q.val}")
        if p.val != q.val:
            return False

    
        traverse_p = self.traverse(p)
        traverse_q = self.traverse(q)

        print(f"traverse_p: {traverse_p}, traverse_q: {traverse_q}")

        if traverse_p != traverse_q:
            return False

        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        
        return False

        # return True
                    