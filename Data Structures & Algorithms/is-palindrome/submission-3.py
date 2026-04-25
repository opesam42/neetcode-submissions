import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(f"Clean string {s_clean}")

        left, right = 0, len(s_clean) - 1

        while left < right:
            print(f"comparing {s_clean[left]} with {s_clean[right]}")
            if s_clean[left] != s_clean[right]:
                return False # that is not a palindrome
            
            left += 1
            right -= 1
        
        return True

sol = Solution()
s1 = "tab a cat"
s2 = "Was it a car or a cat I saw?"
result = sol.isPalindrome(s=s2)
print(f"Result: {result}")