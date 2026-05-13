class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      

        max_length = 0
        char_dict = {} #store char as key and latest occurence index as value
        left = 0
        check_char = set()
        n = len(s)

        if n == 0:
            return max_length
        
        for right in range(n):
            char = s[right]

            if char in char_dict and char_dict[char] >= left:
                left = char_dict[char] + 1
            
            char_dict[char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length    

sol = Solution()
s1 = "zxyzxyz"
s2 = "xxxx"
result = sol.lengthOfLongestSubstring(s1)
print(f"Result: {result}")