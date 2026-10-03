class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}  # key: idx:start
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        def recursion(idx: int, start: int, end: int):
            if idx == start:
                return nums[idx]
            if idx == start + 1:
                return max(nums[idx], nums[idx-1])
            
            key = f"{idx}:{start}"
            if key in cache:
                return cache[key]
            
            result = max(
                nums[idx] + recursion(idx-2, start, end),
                recursion(idx-1, start, end)
            )
            
            cache[key] = result

            return result

        # get the max in from the first house to the second to the last house
        max1 = recursion(
            idx=len(nums)-2,
            start=0,
            end=len(nums) -2
            )
        
        # get the max from the second house to the last house
        max2 = recursion(
            idx=len(nums)-1,
            start=1,
            end=len(nums)-1
        )

        return max(max1, max2)

