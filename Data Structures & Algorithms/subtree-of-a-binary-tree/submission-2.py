from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:   
    def search_by_preorder(self, root, target_root_val):
        if root:
            if root.val == target_root_val:
                # breakpoint()
                return root
            left_search = self.search_by_preorder(root.left, target_root_val)
            if left_search:
                return left_search
            right_search = self.search_by_preorder(root.right, target_root_val)
            if right_search:
                return right_search

        return None

    def traverse_node(self, node):
        left_node, right_node = None, None
        if node:
            if node.left:
               left_node = node.left.val

            if node.right:
                right_node = node.right.val
        
            return (left_node, right_node)
        
        return (None, None)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # handle empty trees
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False

        print(f"p: {p.val}, q: {q.val}")
        if p.val != q.val:
            return False

    
        traverse_p = self.traverse_node(p)
        traverse_q = self.traverse_node(q)

        # print(f"traverse_p: {traverse_p}, traverse_q: {traverse_q}")

        if traverse_p != traverse_q:
            return False

        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pivot_node = self.search_by_preorder(root, subRoot.val)
        if not pivot_node:
            return False
        
        result = self.isSameTree(pivot_node, subRoot)
        if result is False:
            pivot_node.val = "V"
            return self.isSubtree(root, subRoot)
        else:
            return result

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