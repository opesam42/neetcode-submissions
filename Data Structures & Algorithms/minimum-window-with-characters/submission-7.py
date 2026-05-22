class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_dict = {}
        window_dict = {}
        for i in range(len(t)):
            char = t[i]
            if char not in t_dict:
                t_dict[char] = 1
                window_dict[char] = 0
            else:
                t_dict[char] += 1

        have = 0
        need = len(t_dict)
        
        # breakpoint()

        sub_string = ""
        min_length = float('inf')

        left = 0
        right = 0

        while right < len(s):
            char = s[right]
            if char in window_dict:
                window_dict[char] += 1
                

                # check if equal to the value in t_dict
                if window_dict[char] == t_dict[char]:
                    have += 1
            
            # breakpoint()
            while have == need:
                current_length = (right - left + 1)

                # breakpoint()
                if min_length > current_length:
                    min_length = current_length
                    sub_string = s[left:right+1]
                    
                    
                
                # increament left
                char_left = s[left]
                if char_left in window_dict:
                    window_dict[char_left] -= 1

                    # check if the decremented value is still greater or equal to the value in t_dict
                    if window_dict[char_left] < t_dict[char_left]:
                        have -= 1
                left += 1 #shrink window
            
            right += 1

        return sub_string
                



        
        
                

                
                
s1 = "OUZODYXAZV"
t1 = "XYZ"

s2 = "xx"
t2 = "xx"

s3 = "ab"
t3 = "a"

sol = Solution()
result = sol.minWindow(s2, t2)
print(f"Result: {result}")