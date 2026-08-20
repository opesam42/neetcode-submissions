""" Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q are descendants. The ancestor is allowed to be a descendant of itself. """

""" 
    My explanation to the code to an interviewer
    1. Did the solution guarantee that p and q would be present in the tree?
    2. It's a binary tree, right?
    3. Okay - so the first thing to look for the base case
    4. Since the question said that one of the node could be the ancestors
    5. So one of the base case, would be that if the explored root is one of the node, we can return the root
    6. Since it is a binary search tree, this give us the easy route to like know which subtree to traverse
    7. So if both the values are less than the explored root, it mean that the values are at the left sub-tree
    8. If both the values are greater than the explored root, it mean the values are at the right sub-tree
    9. But if one is at the left subtree and the right subtree - then it mean the explored root is the least common ancestors, so return the explored root

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traversal(root):
        if root:
            return (root.left, root.right)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == q or root == p:
            return root
        
        if root.val <= q.val and root.val <= p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if root.val >= p.val and root.val >= q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root

        # return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
        
