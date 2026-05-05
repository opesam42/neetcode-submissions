class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        n = len(height)
        for i in range(n):
            if i == 0 or i == len(height) - 1:
                continue
            
            left_bars = height[0:i]
            right_bars = height[i+1:n]
            
            max_left_bar = max(left_bars)
            max_right_bar = max(right_bars)

            vol = min(max_left_bar, max_right_bar) - height[i]
            if vol < 0:
                continue
            volume += vol

        return volume