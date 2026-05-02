class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = (right-left)
            height = min(heights[left], heights[right])
            area = width * height
            if area > maxArea:
                maxArea = area
            
            # condition for next loop
            # if the left bar is smaller then move 
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1 #doesn't matter at this point when the bar have the same hiehg, one can move the left or right pointer

        return maxArea