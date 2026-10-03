class Solution:
    def rob(self, nums: List[int]) -> int:
        # he we are computing the best option at each point 
        # [3 1 3] at idx = 2 the best option is to rob the current house and the house next to the adjacent or sckip the house and rob the adjacent and then take the max
        # so at idx 2 we can either rob idx 2 and idx 0 -> 3 + 3 = 6 or rob the adjacent house idx 1 -> 1
        # so at idx = 2 the max we can steal is 
        length: int = len(nums)
        cache: dict = {}

        def recursion(idx: int) -> int:
            if idx == 0:
                return nums[idx]

            if idx == 1:
                return max(nums[idx-1], nums[idx])

            if idx in cache:
                return cache[idx]

            result = max(
                nums[idx] + recursion(idx-2),
                recursion(idx-1)
            )

            cache[idx] = result

            return result

        return recursion(length - 1)
