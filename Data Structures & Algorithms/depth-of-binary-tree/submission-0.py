# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        if root is None:
            return 0
            
        if root.left is None:
            left_depth = 0
        else:
            left_depth = self.maxDepth(root.left)
        
        if root.right is None:
            right_depth = 0
        else:
            right_depth = self.maxDepth(root.right)

        max_depth = 1 + max(left_depth, right_depth)
        return max_depth

            
        