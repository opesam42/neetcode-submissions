class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary that stores the numbers in the list and it index
        nums_map = {}
        result = []

        for i in range(len(nums)):
            nums_map[nums[i]] = i

        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1

            if num2 in nums_map and nums_map[num2] != i:
                j = nums_map[num2]
                result.append(i)
                result.append(j)
                break
        
        return result

            