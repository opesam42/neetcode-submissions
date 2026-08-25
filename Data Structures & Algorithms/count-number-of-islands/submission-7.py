class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        explored_nodes = set()
        no_of_island = 0

        for row in range(rows):
            for col in range(cols):
                # print(explored_nodes)
                if grid[row][col] != "1":
                    continue
                
                if (row, col) in explored_nodes:
                    continue

                queue.append((row, col))
               
                self.bfs(grid, row, col, explored_nodes, queue, rows, cols)
                no_of_island += 1
        
        return no_of_island
    

    def bfs(self, grid, row, col, explored_nodes, queue, rows, cols):
        # store the value location in the queue - [row, col]
        # print(queue)

        while len(queue) != 0:
            # check the neighbours of the current element (top, left, right, bottom)
            curr_elem_pos = queue.popleft()

            row = curr_elem_pos[0]
            col = curr_elem_pos[1]

            # move to the bottom
            if row < (rows - 1):
                updated_row = row+1
                if grid[updated_row][col] == "1" and (updated_row, col) not in explored_nodes:
                    queue.append((updated_row, col))
                    explored_nodes.add((updated_row, col))   # mark as explored to prevent it from been added to the queue again (redundant)
            # move to the top
            if row > 0:
                updated_row = row - 1
                if grid[updated_row][col] == "1" and (updated_row, col) not in explored_nodes:
                    queue.append((updated_row, col))
                    explored_nodes.add((updated_row, col)) 
            # move to the left
            if col > 0:
                updated_col = col - 1
                if grid[row][updated_col] == "1" and (row, updated_col) not in explored_nodes:
                    queue.append((row, updated_col))
                    explored_nodes.add((row, updated_col))
            # move to the right
            if col < (cols-1):
                updated_col = col + 1 
                if grid[row][updated_col] == "1" and (row, updated_col) not in explored_nodes:
                    queue.append((row, updated_col))
                    explored_nodes.add((row, updated_col))

            # print(f"Queue: {queue}")
            # print(f"Visited Nodes: {explored_nodes} \n")


            