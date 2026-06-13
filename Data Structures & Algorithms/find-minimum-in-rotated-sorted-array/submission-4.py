from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = 0
        right = n-1

        while left < right:
            mid = (left + right) // 2
            
            # breakpoint()

            # if nums[mid] == nums[left]:
            #     breakpoint()
            #     return nums[mid]

            if nums[mid] > nums[right]:
                # that implies that the first half is not sorted
                left = mid + 1
            else:
                right = mid

            # breakpoint()

            # return self.findMin(nums)
        
        return nums[left]
    
sol = Solution()
result = sol.findMin([3,4,5,6,1,2])
print(f"Result: {result}")

            
            
