from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case1
        if not subRoot:
            return True

        # base case2
        if not root or not subRoot:
            return False

        result = self.isSameTree(root, subRoot)

        if result is False:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return True

        # pivot_node_traverse = self.traverse_node(pivot_node)
        # subroot_node_traverse = self.traverse_node(subRoot)
        # # breakpoint()

        # if pivot_node_traverse != subroot_node_traverse:
        #     return False

        # if subRoot.left:
        #     left_match = self.isSubtree(root.left, subRoot.left)
        #     if not left_match:
        #         return False
        # if subRoot.right:
        #     right_match = self.isSubtree(root.right, subRoot.right)
        #     if not right_match:
        #         return False

        # return True