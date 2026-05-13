class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        set longest to 0
        create a set call check
        for each loop:
            if the element is not in the set:
                add to the set and increament the longest
            elif if element is in the set
                clear check_char set
                append longest to substring_length

            at the end of the loop:
                append the longest atp to the substring_length set
        return max of substring_length
        """
        

        longest = 0
        char_dict = {} #store char as key and latest occurence index as value
        left = 0
        check_char = set()
        substring_length = set()

        n = len(s)

        if n == 0:
            return longest
        
        while left < n:
            for i in range(left, n):
                char = s[i]
                if char not in check_char:
                    check_char.add(char)
                    char_dict[char] = i
                    longest += 1
                    substring_length.add(longest)
                else:
                    check_char.clear()
                    substring_length.add(longest)
                    longest = 0
                    left += 1
                    break
                    
        
        # for i in range(n):
        #     char = s[i]
        #     if char not in check_char:
        #         check_char.add(char)
        #         longest += 1
        #         substring_length.add(longest)
        #     else:
        #         check_char.clear()
        #         substring_length.add(longest)
        #         # reset and add the element to the check_char
        #         ind = s.rindex(char, 0, i)
        #         longest = i - ind
        #         # advdf
        #         check_char.add(char)
            
        return max(substring_length)
            
            
    

sol = Solution()
s1 = "zxyzxyz"
s2 = "xxxx"
result = sol.lengthOfLongestSubstring(s1)
print(f"Result: {result}")