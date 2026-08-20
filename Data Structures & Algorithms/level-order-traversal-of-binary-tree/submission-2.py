''' 
    So traverse the tree level by level.
    1. Is there a way one can know what level one is in a table? None
    2. So we need to look for a way to track it 
    3. So the root is level 0
    4. So as we move to it children, we need to increase the level by 1
    5. So we will need an helper function - that first takes the root as an argument and the set the level at 0
    6. As it move to the next level, it increases the level by 1
    7. At each node explored, it append the node value to the corresponding level of the array.
'''
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
        current_level = 0
        queue = deque()
        if not root:
            return []

        queue.append(root)

        while len(queue) > 0:
            if len(arr) >= current_level:
                arr.append([])
                
            for i in range(len(queue)):
                head = queue[0]
                if head.left is not None:
                    queue.append(head.left)
                if head.right is not None:
                    queue.append(head.right)
                
                arr[current_level].append(head.val)
                queue.popleft()
            
            current_level += 1

        return arr

        # arr = []
        # self.levelOrderByLevel(root, 0, arr)
        # return arr

