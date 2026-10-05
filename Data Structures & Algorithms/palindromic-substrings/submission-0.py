class Solution:
    def countSubstrings(self, s: str) -> int:
        length: int = len(s)
        palindromes: int = 0

        for i in range(length):
            # for odd palindromes
            left: int = i
            right: int = i
            while left >= 0 and right < length and s[left] == s[right]:
                palindromes += 1
                left -= 1
                right += 1

            # for even palindromes
            left = i
            right = i+1
            while left >= 0 and right < length and s[left] == s[right]:
                palindromes += 1
                left -= 1
                right += 1

        return palindromes