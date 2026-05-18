class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_len = 0

        freq_map = {}
        highest_freq = 0
        
        # while right < len(s):
        #     char = s[left]
            
        #     # check if the character is in the frequency map
        #     if char not in freq_map:
        #         freq_map[char] = {
        #             "freq": 0,
        #             "start": left,
        #             "end": right
        #         }

        #     if char == s[right]:
        #         freq_map[char]["freq"] += 1
        #         freq_map[char]["end"] = right
        #         # increament right
        #         right += 1
        #     else:
        #         left = right

        # # select char with high freq and it frequency

        # print(freq_map)

        # # take the char with the maximum frequecny
        # highest_freq = 0
        # freq_char = ""
        # for key, value in freq_map.items():
        #     if max(value["freq"], highest_freq) == value["freq"]:
        #         freq_char = key
        #         highest_freq = value["freq"]
        #         freq_char_start = value["start"]
        #         freq_char_end = value["end"]
        
        # # freq_char_dict = {freq_char: freq_map[freq_char]}
        
        # print(f"Char with highest freq is {freq_char} with a frequency of {highest_freq}")

        left = 0
        right = 0
        while right < len(s):
            char = s[right]
            if char not in freq_map:
                freq_map[char] = {
                    "freq": 0,
                    "start": left,
                    "end": right
                }

            if char == s[right]:
                freq_map[char]["freq"] += 1
                freq_map[char]["end"] = right
            
            highest_freq = max(highest_freq, freq_map[char]["freq"])

            window_len = (right - left) + 1
            chars_to_replace = window_len - highest_freq

            while chars_to_replace > k:
                char_left = s[left]

                # Decrement the character we are leaving behind
                freq_map[char_left]["freq"] -= 1

                left += 1

                chars_to_replace = (right - left + 1) - highest_freq

            max_len = max(max_len, right-left+1)
            right += 1
        
        return max_len

    """   left = 0
        right = len(s) - 1

        while right != left:
            substring_len = (right - left) + 1
            if substring_len > highest_freq + k:
                if right > freq_char_end:
                    right -= 1
            #     elif left < freq_char_start:
            #         left += 1
            #     else:
            #         pass
            # elif right - left < highest_freq + k
            else:
                # substring = s[left:right]
                print(f" starts at {left} ends at {right}")
                # max_len = len(substring)
                max_len = right - left + 1
                break

        return max_len
        # return freq_map 
    """




sol = Solution()
s1 = "XYYX"
k1 = 2

s2 = "AAABABB"
k2 = 1

s3 = "AABABBA"
k3 = 1

result1 = sol.characterReplacement(s1, k1)
print(f"Result1: {result1}\n")

result2 = sol.characterReplacement(s2, k2)
print(f"Result2: {result2}")

result3 = sol.characterReplacement(s3, k3)
print(f"Result2: {result3}")