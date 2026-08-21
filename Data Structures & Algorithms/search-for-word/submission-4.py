from typing import List

class Solution:
    def dfs(self, row, col, index, visited, board, word):
        board_char = board[row][col]
        rows = len(board)
        cols = len(board[0])

        # if index == len(word):
        #     return True

        cell = f"({row}, {col})"
        if cell in visited:
            return False
        
        char = word[index]

        if char == board_char:
            visited.add(cell)

            # check if we have gotten to the end
            index = index+1
            if index == len(word):
                return True

            if row > 0:
                if self.dfs(row-1, col, index, visited, board, word):
                    return True
            if row < rows - 1:
                if self.dfs(row+1, col, index, visited, board, word):
                    return True
            if col > 0:
                if self.dfs(row, col-1, index, visited, board, word):
                    return True
            if col < cols - 1:
                if self.dfs(row, col+1, index, visited, board, word):
                    return True

            # backtrack
            visited.remove(cell)

        return False
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if self.dfs(row, col, 0, visited, board, word):
                    return True

        return False

        

# board=[
#     ["C","A","A"],
#     ["A","A","A"],
#     ["B","C","D"]
# ]
# word="AAB"

# sol = Solution()

# print(sol.exist(board, word))