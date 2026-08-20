# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderByLevel(self, root, level, arr):
        # base case
        if root is None:
            return

        if level >= len(arr):
            arr.append([])
        
        arr[level].append(root.val)

        self.levelOrderByLevel(root.left, level+1, arr)
        self.levelOrderByLevel(root.right, level+1, arr)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        self.levelOrderByLevel(root, 0, arr)
        return arr

