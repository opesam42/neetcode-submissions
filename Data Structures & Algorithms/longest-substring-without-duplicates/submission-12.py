class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        if len(s) == 0:
            return 0
        left = 0
        max_length = 0
        char_set = {} #key is the character, the value is the last occurence of the character

        for right in range(len(s)):
            char = s[right]
            if char in char_set and char_set[char] >= left:
                left = char_set[char] + 1

            char_set[char] = right
            length = (right-left) + 1
            max_length = max(max_length, (right-left)+1)
        
        return max_length

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