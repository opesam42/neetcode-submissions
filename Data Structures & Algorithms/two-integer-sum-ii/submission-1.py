class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        output = []

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            if sum > target:
                right -= 1
            if sum == target:
                # just append the indices (not the values of the indices)
                # recall it is one-indexed
                output.append(left+1)
                output.append(right+1)
                break

        return output



                