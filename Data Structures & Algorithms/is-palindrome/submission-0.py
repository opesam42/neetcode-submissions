import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_trim = s.replace(" ", "") # remove space from strng
        s_clean = ( re.sub(r'[^a-zA-Z0-9]', '', s_trim) ).lower()
        print(f"Clean string {s_clean}")
        s_list = list(s_clean)

        left, right = 0, len(s_list) - 1

        while left < right:
            print(f"comparing {s_list[left]} with {s_list[right]}")
            if s_list[left] != s_list[right]:
                return False # that is not a palindrome
            
            left += 1
            right -= 1
        
        return True

sol = Solution()
s1 = "tab a cat"
s2 = "Was it a car or a cat I saw?"
result = sol.isPalindrome(s=s2)
print(f"Result: {result}")