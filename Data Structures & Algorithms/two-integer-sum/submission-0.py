class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_array = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    sum_array.append(i)
                    sum_array.append(j)
                    return sum_array
        return sum_array