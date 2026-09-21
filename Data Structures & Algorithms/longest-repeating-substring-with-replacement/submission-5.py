class Solution:
    def characterReplacement(self, s: str, k: int):
        max_len = 0

        char_map = {}

        left = 0

        for right in range(len(s)):
            highest_freq = 0

            char = s[right]
            # increment the freq of char in the map
            if char not in char_map:
                char_map[char] = 1
            else:
                char_map[char] += 1

            # get the highest frequency
            highest_freq = max(highest_freq, char_map[char])

            for freq in char_map.values():
                highest_freq = max(highest_freq, freq)

            window_len = (right - left) + 1


            no_of_replacement = window_len - highest_freq

            # for replacement to occur the no_of_replacement must be less than or equal to k  
            while no_of_replacement > k:
                # move the left pointer and decrement the frequency of the char at the left before moving the pointer
                left_char = s[left]
                char_map[left_char] -= 1
                left += 1

                # recalculate hightest_freq
                highest_freq = 0
                for freq in char_map.values():
                    highest_freq = max(highest_freq, freq)
                
                no_of_replacement = (right - left + 1) - highest_freq

            fit_window_len = (right - left) + 1
            max_len = max(max_len, fit_window_len)
    
        return max_len
