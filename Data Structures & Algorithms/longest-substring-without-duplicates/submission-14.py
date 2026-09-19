class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        maxLength = 0
        char_map = {}

        n = len(s)

        if n == 0:
            return 0

        left, right = 0, 0

        while right < len(s):
            curr_char = s[right]

            # if the curr char is in hashmap
            # compare the idx in the hashmap with the idx of the left pointer to check if it is in the same window
            if curr_char in char_map and char_map[curr_char] >= left:
                # it is in the window
                left = char_map[curr_char] + 1
            
            char_map[curr_char] = right
            maxLength = max(maxLength, (right-left+1))
            right += 1

        return maxLength

        # if len(s) == 0:
        #     return 0    
        # left, right = 0,0
        # lenghts = []

        # while left < len(s):
        #     # print(f"Left: {left}, Right: {right}")
        #     char_set = set()
        #     while right < len(s):
        #         char = s[right]
                
        #         if char in char_set:
        #             break
        #         char_set.add(char)
        #         right += 1

        #     lenghts.append(len(char_set))
        #     left += 1
        #     right = left

        # max_length = max(lenghts)

        # return max_length

# s = "aab"
# sol = Solution()
# print(sol.lengthOfLongestSubstring(s))