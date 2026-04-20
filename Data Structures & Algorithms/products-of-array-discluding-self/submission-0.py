from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            print(f"Finding the output[{i}]")

            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product = product * nums[j]

            print(f"Output of {nums[i]} is {product}")
            output.append(product)

        return output