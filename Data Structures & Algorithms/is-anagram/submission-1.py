class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # convert s to list of chars
        s_list = list(s)
        t_list = list(t)

        # check if length are equal, especially for extra chars which are repeated
        if len(s_list) != len(t_list):
            return False
        
        # loop through s and check if all char in s is also in t
        for char in s_list:
            if not char in t_list:
                return False
            else:
                # remove the character to prevent being used to compare
                t_list.remove(char)
            
        return True

        