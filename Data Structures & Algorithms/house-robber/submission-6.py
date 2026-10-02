class Solution:
    def rob(self, nums: List[int]) -> int:
        length: int = len(nums)
        cache: dict = {}

        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])

        def recursion(idx: int)  -> int:
            if idx == 0 or idx == 1:
                cache[idx] = nums[idx]
                return nums[idx]

            if idx in cache:
                return cache[idx]

            weight: int = nums[idx]
            result: int = 0
            for i in range(idx-2, -1, -1):
                temp_sum: int = weight + recursion(i)
                result = max(result, temp_sum)
                # print(f"Woring on  {idx} - {i} gives {recursion(i)} - result: {result}")

            cache[idx] = result

            return result

        for i in range(0, length):
            recursion(i)

        return max(list (cache.values() ))

    