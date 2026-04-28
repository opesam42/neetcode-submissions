from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range( len(nums) ):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right] + nums[i]
                
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1
                    
                    # 3. NOW skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # 4. NOW skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                    

        return output


sol = Solution()
nums = [-4, -1, -1, 0, 1, 2]
nums2 = [0, 0, 0, 0, 0, 0]
result = sol.threeSum(nums)
print(f"Result: {result}")