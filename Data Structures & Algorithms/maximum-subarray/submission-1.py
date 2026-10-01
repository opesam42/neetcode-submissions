class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                # reset to zero when the curr sum is less than zero - reset to 0
                curr_sum = 0
            curr_sum += num
            max_sub = max(max_sub, curr_sum)

        return max_sub



    def maxSubArray_1(self, nums: List[int]) -> int:
        curr_max = float('-inf')
        start = None
        end = None

        for left in range(len(nums)):
            sum = 0
            right = left
            while right < len(nums):
                sum += nums[right]
                if sum >= curr_max:
                    curr_max = sum
                    start = left
                    end = right
                
                right += 1
        
        return curr_max
