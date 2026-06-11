class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        current = nums[0]
        right = n-1

        while right >= 0:
            if current > nums[right]:
                current = nums[right]
                right -= 1
            else:
                return current
            
            
