from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized_list = []
        if root is None:
            serialized_list.append("#")
            print(serialized_list)
            return "-".join(serialized_list)
            
        q = deque()
        q.append(root)
        

        while len(q) != 0:
            curr_node = q.popleft()
            if curr_node == "#":
                serialized_list.append("#")
                continue

            serialized_list.append(str(curr_node.val))

            if curr_node.left:
                q.append(curr_node.left)
            else:
                q.append("#")
            if curr_node.right:
                q.append(curr_node.right)
            else:
                q.append("#")

        list_string = "-".join(serialized_list)
        print(list_string)
        return list_string

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split("-")
        if arr[0] == "#":
            return None
        
        q = deque()
        root = TreeNode(arr[0])
        q.append(root)

        i = 1
        while len(q) != 0:
            curr_node = q.popleft()

            # left node
            if arr[i] != "#":
                print(arr[i])
                left_node = TreeNode(arr[i])
                curr_node.left = left_node
                q.append(left_node)
            i += 1

            # right node
            if arr[i] != "#":
                right_node = TreeNode(arr[i])
                curr_node.right = right_node
                q.append(right_node)
            i += 1

        return root
