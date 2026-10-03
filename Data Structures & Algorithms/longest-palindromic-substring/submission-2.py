
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        # at each idx find the longest substring 
        length = len(s)

        max_len = 0
        max_sub = ""

        for i in range(len(s)):
            pivot_char = s[i]

            # for odd palindrome
            left, right = i, i
            while left >= 0 and right < length and s[left] == s[right]:
                s_len = (right - left + 1)
                if s_len > max_len:
                    max_len = s_len
                    max_sub = str( s[left:right+1] )

                left -= 1
                right += 1


            # for even palindrome
            left, right = i, i+1
            while left >= 0 and right < length:
                s_len = (right - left + 1)
                if s[right] == s[left]:
                    if s_len > max_len:
                        max_len = s_len
                        max_sub = str( s[left:right+1] )
                else:
                    break

                left -= 1
                right += 1
                    


        return max_sub