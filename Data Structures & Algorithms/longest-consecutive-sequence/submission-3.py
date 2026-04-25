class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_dict = {}
        longest_length = 0
        
        for num in nums_set:
            if (num-1) not in nums_set:
                count = 0
                while num in nums_set:
                    count += 1
                    num += 1
                longest_length = max(longest_length, count)        

        return longest_length
        


sol = Solution()
result = sol.longestConsecutive([1, 2, 3, 10, 11, 12])
print(f"Result: {result}")
                        
