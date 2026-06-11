class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        first_elem = nums[0]
        last_elem = nums[n-1]
        
        # if first_elem < last_elem:
        #     return first_elem
        
        current = first_elem
        right = n-1

        while right >= 0:
            if current > nums[right]:
                current = nums[right]
                right -= 1
            else:
                return current
            
            
