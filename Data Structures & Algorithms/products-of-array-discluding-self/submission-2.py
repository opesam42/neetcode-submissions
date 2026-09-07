class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * n
        suffix_prod = [1] * n
        product_arr = [1] * n

        left_prod = 1
        for i in range(n):
            prefix_prod[i] = left_prod 
            left_prod = left_prod * nums[i]
        
        right_prod = 1
        for i in range(n-1, -1, -1):
            suffix_prod[i] = right_prod
            right_prod = right_prod * nums[i]
    
        for i in range(n):
            product_arr[i] = prefix_prod[i] * suffix_prod[i]

        return product_arr
        