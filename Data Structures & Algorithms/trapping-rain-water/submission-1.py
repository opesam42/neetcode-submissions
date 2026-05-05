class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        left_max[0] = height[0]

        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        print(f"left max: {left_max}")

        right_max = [0] * n
        right_max[-1] = height[-1]
        # loop ends at -1 so as to include the 0th index
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        print(f"Right max: {right_max}")


        volume = 0
        for i in range(1, n-1):
            vol = min(left_max[i-1], right_max[i+1]) - height[i]
            
            if vol < 0:
                continue
            print(f"Trapped water @ {i} is {vol}")
            volume += vol

        return volume