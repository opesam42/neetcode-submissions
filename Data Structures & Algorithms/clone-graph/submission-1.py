# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self) -> None:
       self.visited = {}
    
    def cloneNodes(self, node: Optional['Node']):
        # return a hashmap
        new_node = Node(node.val)
        self.visited[node] = new_node

        # explore the node neighbours
        for neighbor in node.neighbors:
            # check if the neighbor have been cloned
            if neighbor not in self.visited:
                self.cloneNodes(neighbor)
    
    def connectNodes(self, node):
        for neighbor in node.neighbors:
            cloned_node = self.visited[node]
            # stopping condition - is if the node is already a neighbor
            if self.visited[neighbor] in cloned_node.neighbors:
                return
            cloned_node.neighbors.append(self.visited[neighbor])
            self.connectNodes(neighbor)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
     

        self.cloneNodes(node)
        self.connectNodes(node)

        return self.visited[node]