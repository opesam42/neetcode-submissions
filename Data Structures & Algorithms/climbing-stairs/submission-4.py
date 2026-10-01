class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def climbStairs(self,n: int) -> int:
        def recursion(current_stair = n):
            # base case
            if current_stair == 0 or current_stair == 1:
                return 1

            if current_stair in self.cache:
                return self.cache[current_stair]
            
            result = recursion(current_stair-1) + recursion(current_stair- 2)
            self.cache[current_stair] = result

            return result

        return recursion(n)